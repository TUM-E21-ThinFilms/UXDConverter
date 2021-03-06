import os

from uxdconverter.ui.gui import Ui_UXDConverter
from uxdconverter.ui.graph import Plotting
from uxdconverter.converter import Converter
from uxdconverter.exporter import FileExporter, ParrattExportAlgorithm, ORSOExportAlgorithm
from uxdconverter.measurement import MeasurementContext, Measurements

from PyQt5.QtWidgets import QFileDialog, QTreeWidgetItem, QHeaderView, QMessageBox
from PyQt5.QtCore import Qt, pyqtSignal, QObject

from uxdconverter.parser.general import GeneralParser
from uxdconverter.ui.controllers.xrd import XrdControllerTab
from uxdconverter.ui.controllers.conversion import ConversionControllerTab
from uxdconverter.util import get_logger

class SignalPropagator(QObject):
    sig = pyqtSignal(list)


class Controller(object):
    def __init__(self, ui: Ui_UXDConverter, app):

        self.app = app
        self.ui = ui
        self.logger = get_logger(__name__)
        self.measurements = None
        self.files = []
        self._plotting = Plotting()
        self.setup()
        self._parser = GeneralParser()

        self._sub_controller = [XrdControllerTab(ui, app), ConversionControllerTab(ui, app)]

    def run(self):
        pass

    def setup(self):
        self.ui.pushButton_input.clicked.connect(self.select_file_input)
        self.ui.pushButton_output.clicked.connect(self.select_file_output)
        # self.ui.lineEdit_input.returnPressed.connect(self.read_file)
        self.ui.pushButton_convert.clicked.connect(self.convert)
        self.ui.pushButton_plot.clicked.connect(self.plot)
        self.ui.pushbutton_select_graph.clicked.connect(self.plot_with_selection)
        self.ui.pushButton_preview.clicked.connect(self.plot_preview)
        self.ui.checkBox_convert_qz.clicked.connect(self.update_label_cropping)

        self.ui.pushButton_deletefile.clicked.connect(self.delete_file)
        self.ui.pushButton_addfile.clicked.connect(self.add_file)
        self.ui.pushButton_resetfile.clicked.connect(self.reset)

    def update_manual_normalization(self, xy_data_point):
        if xy_data_point is None:
            return

        norm = 1 / float(xy_data_point[1])
        self.logger.debug("Normalization factor: {}".format(norm))
        #print("Normalization factor: %s" % str(norm))
        self.ui.lineEdit_normalization_factor.setText(str(norm))

    def check_file(self, file):
        try:
            ms = self._parser.parse(file, self.logger)

            if ms is not None:
                return ms.get_count_measurements() + ms.get_count_background_measurements()

        except BaseException as e:
            self.logger.exception(e)

        return 0

    def reset(self, arbitrary_qt_data=None, message_box=True):
        if message_box is True:
            msg = QMessageBox()
            ret = msg.information(None, "Reset files",
                                  "Are you sure to reset all files?",
                                  buttons=QMessageBox.Ok | QMessageBox.Cancel)
            if ret == QMessageBox.Cancel:
                return

        self.ui.lineEdit_input.setText("")
        self.ui.lineEdit_output.setText("")
        self.measurements = None
        self.files = []
        self.update_measurement_view()
        self.update_file_list()

    def delete_file(self):
        root = self.ui.treeWidget_file.invisibleRootItem()
        child_count = root.childCount()
        for i in reversed(range(child_count)):
            item = root.child(i)

            if item.isSelected():
                index = item.data(0, Qt.UserRole)
                del self.files[index]

        if len(self.files) == 0:
            self.reset(message_box=False)

        self.update_file_list()
        self.read_files()

    def read_files(self):

        self.measurements = None
        for file in self.files:
            try:
                ms = self._parser.parse(file, self.logger)

                for measurement in ms.get_measurements():
                    measurement.file_name = file

                if self.measurements is None:
                    self.measurements = ms
                else:
                    self.measurements.add(ms)

            except BaseException as e:
                self.logger.exception(e)

        self.update_measurement_view()

    def add_file(self, file=None):
        if file is None or not isinstance(file, str):
            file = self.ui.lineEdit_input.text()

        if file == "":
            return

        # check for duplicate files
        for f in self.files:
            if file == f:
                msg = QMessageBox()
                ret = msg.information(None, "Input file", "The selected input file already exists in the file list. ",
                                      buttons=QMessageBox.Ok)
                return

        if self.check_file(file) == 0:
            msg = QMessageBox()
            ret = msg.information(None, "Input file", "Could not read file %s." % file,
                                  buttons=QMessageBox.Ok)
            return

        self.files.append(file)
        self.update_file_list()
        self.read_files()

    def update_file_list(self):
        self.ui.treeWidget_file.clear()
        if self.files is []:
            return

        for i, file in enumerate(self.files):
            item = QTreeWidgetItem(self.ui.treeWidget_file)
            item.setFlags(item.flags() | Qt.ItemIsSelectable)
            item.setText(0, "File %s" % self.shortify_path(file, 55))  #

            fullpath = QTreeWidgetItem(item)
            fullpath.setText(0, "Path: %s" % file)
            fullpath.setFlags(fullpath.flags() ^ Qt.ItemIsSelectable)

            mscount = QTreeWidgetItem(item)
            mscount.setText(0, "Measurement count: %s" % self.check_file(file))
            mscount.setFlags(mscount.flags() ^ Qt.ItemIsSelectable)
            item.setData(0, Qt.UserRole, i)

    def select_file_input(self):
        files = QFileDialog.getOpenFileNames(filter="UXD/RAW/DAT (*.uxd *.raw *.dat);;UXD (*.uxd);;RAW (*.raw);;DAT (*.dat);;All *.*")[0]
        if len(files) == 0:
            return

        self.ui.lineEdit_input.setText(files[0])
        if self.ui.lineEdit_output.text() == "":
            self.ui.lineEdit_output.setText(files[0].replace('.UXD', '') + ".dat")
            self.ui.lineEdit_output.setText(files[0].replace('.raw', '') + ".dat")

        if len(files) > 1:
            for f in files:
                self.add_file(f)

    def select_file_output(self):
        self.ui.lineEdit_output.setText(QFileDialog.getOpenFileName()[0])

    def add_measurement(self, measurement, name, id, is_background=False):
        # context = self.create_context()

        item = QTreeWidgetItem(self.ui.measurements)
        item.setFlags(item.flags() | Qt.ItemIsSelectable | Qt.ItemIsEditable)
        item.setText(0, name)
        item.setData(0, Qt.UserRole, id)
        item.setData(1, Qt.UserRole, is_background)
        item.setData(2, Qt.UserRole, measurement.file_name)

        region = QTreeWidgetItem(item)
        data_region = measurement.get_data_region_x()
        region.setText(0, "Theta [deg]: %s ... %s" % (data_region[1], data_region[0]))
        # region.setText(1, "Qz [Ang]: %s ... %s" % (datapoint_to_qz(data_region[1], context), datapoint_to_qz(data_region[0], context)))
        region.setFlags(region.flags() ^ Qt.ItemIsSelectable)



        if not measurement.get_psi() == 0:
            region.setText(1, "Psi [deg]: {}".format(measurement.get_psi()))

        include = QTreeWidgetItem(item)
        include.setText(0, "Include")
        include.setText(1, "Background")
        include.setFlags((include.flags() | Qt.ItemIsUserCheckable) ^ Qt.ItemIsSelectable)
        include.setCheckState(0, Qt.Checked)

        if is_background:
            include.setCheckState(1, Qt.Checked)
        else:
            include.setCheckState(1, Qt.Unchecked)

        if measurement.file_name is not None:
            file = QTreeWidgetItem(item)
            file.setText(0, "File: {}".format(self.shortify_path(measurement.file_name, 30)))
            file.setFlags(region.flags() ^ Qt.ItemIsSelectable)
            file.setToolTip(0, measurement.file_name)

    def update_measurement_view(self):
        self.ui.measurements.clear()
        if self.measurements is None:
            return

        for i, ms in enumerate(self.measurements.get_measurements()):
            self.add_measurement(ms, "Measurement %s" % (i + 1), i, False)

        for i, ms in enumerate(self.measurements.get_background_measurements()):
            self.add_measurement(ms, "Background %s" % (i + 1), i, True)

        self.ui.measurements.header().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.ui.measurements.header().setSectionResizeMode(1, QHeaderView.ResizeToContents)

    def convert(self):

        output = self.ui.lineEdit_output.text()
        if output == "":
            msg = QMessageBox()
            msg.warning(None, "No output file", "No output file given")
            return

        output_path = os.path.dirname(os.path.realpath(output))

        try:
            if not os.path.exists(output_path):
                msg = QMessageBox()
                ret = msg.information(None, "Output Directory",
                                      "The directory does not exist. Do you want to create it?",
                                      buttons=QMessageBox.Ok | QMessageBox.Cancel)
                if ret == QMessageBox.Cancel:
                    return

                os.mkdir(output_path)
        except:
            self.logger.warning('Exception while creating path %s', output_path)
            pass

        try:
            measurements = self.setup_measurement()
            ms = Converter(measurements).convert()
        except BaseException as e:
            self.logger.exception(e)
            return

        if os.path.exists(output):
            msg = QMessageBox()
            ret = msg.information(None, "Output file", "The output file already exists. Do you want to overwrite it?",
                                  buttons=QMessageBox.Ok | QMessageBox.Cancel)

            if ret == QMessageBox.Cancel:
                return

        export_algo = ORSOExportAlgorithm(ms, measurements.get_context())
        export_algo.set_used_data_files([ms.file_name for ms in measurements.get_measurements()])
        export_algo.set_used_background_files([ms.file_name for ms in measurements.get_background_measurements()])
        #export_algo = ParrattExportAlgorithm(ms, measurements.get_context())
        exporter = FileExporter(output, export_algo)

        exporter.do_export()

        if self.ui.checkBox_view_plot.isChecked():
            self._plotting.plot([ms], measurements.get_context())

    def plot(self):

        measurements = []
        background = []

        names_measurement = []
        names_background = []

        # Find the appropriate measurements and background
        root = self.ui.measurements.invisibleRootItem()
        child_count = root.childCount()
        for i in range(child_count):
            item = root.child(i)

            if item.isSelected():
                index = item.data(0, Qt.UserRole)
                is_background = item.data(1, Qt.UserRole)
                if is_background:
                    background.append(self.measurements.get_background_measurements()[index])
                    names_background.append(item.text(0))
                else:
                    measurements.append(self.measurements.get_measurements()[index])
                    names_measurement.append(item.text(0))

        if len(measurements + background) == 0:
            return

        ctx = self.create_context()
        # Set it to false, to display theta values
        ctx.qz_conversion = False

        self._plotting.plot(measurements + background, ctx, names_measurement + names_background, True)

    def plot_preview(self):
        try:
            measurements = self.setup_measurement()

            ms = Converter(measurements).convert()
        except BaseException as e:
            self.logger.exception(e)
            return

        self._plotting.plot([ms], self.create_context())

    def setup_measurement(self):
        measurements = []
        background = []

        # Find the appropriate measurements and background
        root = self.ui.measurements.invisibleRootItem()
        child_count = root.childCount()

        if child_count == 0:
            raise RuntimeError("No measurements available")

        for i in range(child_count):
            item = root.child(i)

            index = item.data(0, Qt.UserRole)
            is_background = False

            if item.child(1).checkState(0) == Qt.Unchecked:
                continue

            if item.child(1).checkState(1) == Qt.Checked:
                is_background = True

            if item.data(1, Qt.UserRole):
                ms = self.measurements.get_background_measurements()[index]
            else:
                ms = self.measurements.get_measurements()[index]

            if is_background:
                background.append(ms)
            else:
                measurements.append(ms)

        return Measurements(self.measurements.get_headers(), measurements, background, self.create_context())

    def plot_with_selection(self):
        context = self.create_context()
        context.normalization = 1.0

        if self.measurements is None:
            self.logger.warning("No plotting since no measurements are available")
            return

        self.measurements.set_context(context)
        ms = Converter(self.measurements).convert()
        # ms = convert_measurement(self.measurements)

        signalPropagator = SignalPropagator()
        signalPropagator.sig.connect(self.update_manual_normalization)
        selection = self._plotting.interactive_plot(ms, signalPropagator)

        if selection is None:
            return

        self.ui.lineEdit_normalization_factor.setText(str(1.0 / selection[1]))

    def update_label_cropping(self):
        if self.ui.checkBox_convert_qz.isChecked():
            self.ui.label_cropping.setText("Qz range [A^-1]")
        else:
            self.ui.label_cropping.setText("Theta range [deg]")

    def create_context(self):
        """
        Creates a measurement context using the user input from the 'Settings' tab
        :return: MeasurementContext
        """
        context = MeasurementContext()
        context.wavelength = float(self.ui.lineEdit_wavelength.text().replace(',', '.'))
        context.average_overlapping = bool(self.ui.checkbox_average.isChecked())
        context.knife_edge = bool(self.ui.checkBox_knifeedge.isChecked())
        context.sample_length = float(self.ui.lineEdit_sample_length.text().replace(',', '.'))
        context.xray_width = float(self.ui.lineEdit_beam_width.text().replace(',', '.'))
        context.qz_conversion = bool(self.ui.checkBox_convert_qz.isChecked())
        context.y_log_scale = bool(self.ui.checkbox_plotLogScale.isChecked())

        context.wavelength_error = float(self.ui.input_wavelength_error.text().replace(',', '.'))
        context.theta_error = float(self.ui.input_theta_error.text().replace(',', '.'))

        range_1, range_2 = float(self.ui.lineEdit_qz_range_min.text().replace(',', '.')), float(
            self.ui.lineEdit_qz_range_max.text().replace(',', '.'))
        context.qz_range = (min(range_1, range_2), max(range_1, range_2))

        if self.ui.radioButton_flank.isChecked():
            context.normalization = 'flank'
        elif self.ui.radioButton_maximum.isChecked():
            context.normalization = 'max'
        elif self.ui.radioButton_manual.isChecked():
            context.normalization = float(self.ui.lineEdit_normalization_factor.text().replace(',', '.'))

        return context

    def shortify_path(self, path, length):

        if len(path) <= length:
            return path

        if length <= 0:
            return path[-length + 1:]

        path = os.path.normpath(path)
        file = os.path.split(path)[1]

        if len(file) > length:
            return "..." + file[-length:]

        mod_path = path
        prev_file = file
        while len(file) < length:
            prev_file = file
            mod_path = os.path.dirname(mod_path)
            file = path[+len(mod_path) - len(path):]

        return "..." + prev_file
