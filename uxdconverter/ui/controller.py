import os
import codecs
import logging

from uxdconverter.ui.gui import Ui_UXDConverter
from uxdconverter.ui.graph import Plotting
from uxdconverter.parser import MeasurementsParser
from uxdconverter.converter import Converter
from uxdconverter.exporter import FileExporter, ParrattExportAlgorithm
from uxdconverter.measurement import MeasurementContext, Measurements

from PyQt5.QtWidgets import QFileDialog, QTreeWidgetItem, QHeaderView, QMessageBox
from PyQt5.QtCore import Qt, pyqtSignal, QObject


class SignalPropagator(QObject):
    sig = pyqtSignal(list)


class Controller(object):
    def __init__(self, ui: Ui_UXDConverter, app):

        self.app = app
        self.ui = ui
        self.logger = self.get_logger(__name__)
        self.measurements = None
        self._plotting = Plotting()
        self.setup()

    def get_logger(self, name):
        """
        Creates a logger with given name
        :param str name:
        :return: logging object
        """
        logger = logging.getLogger(name)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        return logger

    def run(self):
        pass

    def setup(self):
        self.ui.pushButton_input.clicked.connect(self.select_file_input)
        self.ui.pushButton_output.clicked.connect(self.select_file_output)
        self.ui.lineEdit_input.returnPressed.connect(self.read_file)
        self.ui.pushButton_convert.clicked.connect(self.convert)
        self.ui.pushButton_plot.clicked.connect(self.plot)
        self.ui.pushbutton_select_graph.clicked.connect(self.plot_with_selection)

    def update_manual_normalization(self, xy_data_point):
        if xy_data_point is None:
            return

        norm = 1 / float(xy_data_point[1])
        print("Normalization factor: %s" % str(norm))
        self.ui.lineEdit_normalization_factor.setText(str(norm))

    def read_file(self, file=None):
        if file is None:
            file = self.ui.lineEdit_input.text()

        if file is "":
            return

        self.measurements = None

        try:
            self.measurements = MeasurementsParser(codecs.open(file, 'r', encoding='utf-8', errors='ignore'),
                                                   self.logger).parse()
        except BaseException as e:
            self.logger.exception(e)

        self.update_measurement_view()

    def select_file_input(self):
        file = QFileDialog.getOpenFileName()[0]
        if file is "":
            return
        self.ui.lineEdit_input.setText(file)
        self.read_file(file)
        self.ui.lineEdit_output.setText(file.replace('.UXD', '') + ".dat")

    def select_file_output(self):
        self.ui.lineEdit_output.setText(QFileDialog.getOpenFileName()[0])

    def add_measurement(self, measurement, name, id, is_background=False):
        # context = self.create_context()

        item = QTreeWidgetItem(self.ui.measurements)
        item.setFlags(item.flags() | Qt.ItemIsSelectable)
        item.setText(0, name)
        item.setData(0, Qt.UserRole, id)
        item.setData(1, Qt.UserRole, is_background)

        region = QTreeWidgetItem(item)
        data_region = measurement.get_data_region_x()
        region.setText(0, "Theta [deg]: %s ... %s" % (data_region[1], data_region[0]))
        # region.setText(1, "Qz [Ang]: %s ... %s" % (datapoint_to_qz(data_region[1], context), datapoint_to_qz(data_region[0], context)))
        region.setFlags(region.flags() ^ Qt.ItemIsSelectable)

        include = QTreeWidgetItem(item)
        include.setText(0, "Include")
        include.setText(1, "Background")
        include.setFlags((include.flags() | Qt.ItemIsUserCheckable) ^ Qt.ItemIsSelectable)
        include.setCheckState(0, Qt.Checked)

        if is_background:
            include.setCheckState(1, Qt.Checked)
        else:
            include.setCheckState(1, Qt.Unchecked)

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

        print("converting...")

        output = self.ui.lineEdit_output.text()
        if output is "":
            msg = QMessageBox()
            msg.warning(None, "No output file", "No output file given")
            return

        measurements = self.setup_measurement()

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

        exporter = FileExporter(output, ParrattExportAlgorithm())
        exporter.do_export(ms)

        if self.ui.checkBox_view_plot.isChecked():
            self._plotting.plot([ms])

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

        self._plotting.plot(measurements + background, names_measurement + names_background)

    def setup_measurement(self):
        measurements = []
        background = []

        # Find the appropriate measurements and background
        root = self.ui.measurements.invisibleRootItem()
        child_count = root.childCount()
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

        self.measurements.set_context(context)
        ms = Converter(self.measurements).convert()
        # ms = convert_measurement(self.measurements)

        signalPropagator = SignalPropagator()
        signalPropagator.sig.connect(self.update_manual_normalization)
        selection = self._plotting.interactive_plot(ms, signalPropagator)

        if selection is None:
            return

        self.ui.lineEdit_normalization_factor.setText(str(1.0 / selection[1]))

    def create_context(self):
        context = MeasurementContext()
        context.wavelength = float(self.ui.lineEdit_wavelength.text().replace(',', '.'))
        context.average_overlapping = bool(self.ui.checkbox_average.isChecked())
        context.knife_edge = bool(self.ui.checkBox_knifeedge.isChecked())
        context.sample_length = float(self.ui.lineEdit_sample_length.text().replace(',', '.'))
        context.xray_width = float(self.ui.lineEdit_beam_width.text().replace(',', '.'))

        if self.ui.radioButton_flank.isChecked():
            context.normalization = 'flank'
        elif self.ui.radioButton_maximum.isChecked():
            context.normalization = 'max'
        elif self.ui.radioButton_manual.isChecked():
            context.normalization = float(self.ui.lineEdit_normalization_factor.text().replace(',', '.'))

        return context
