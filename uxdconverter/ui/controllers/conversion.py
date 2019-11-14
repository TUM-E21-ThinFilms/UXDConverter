import math

from uxdconverter.ui.gui import Ui_UXDConverter


class ConversionControllerTab(object):

    def __init__(self, ui: Ui_UXDConverter, app):
        self.ui = ui
        self.app = app

        self.setup()

    def setup(self):
        self.ui.conversion_to_qz.toggled.connect(self.update_conversion)
        self.ui.conversion_to_theta.toggled.connect(self.update_conversion)

        self.ui.conversion_input_qz.textEdited.connect(self.update_conversion)
        self.ui.conversion_input_theta.textEdited.connect(self.update_conversion)

        self.ui.conversion_input_theta.editingFinished.connect(self.update_radio)
        self.ui.conversion_input_theta.editingFinished.connect(self.update_radio)
        self.ui.conversion_input_qz.selectionChanged.connect(self.update_radio)
        self.ui.conversion_input_theta.selectionChanged.connect(self.update_radio)

    def update_radio(self):
        if self.ui.conversion_input_theta.hasFocus():
            self.ui.conversion_to_qz.setChecked(True)
        elif self.ui.conversion_input_qz.hasFocus():
            self.ui.conversion_to_theta.setChecked(True)

    def update_conversion(self):
        try:
            theta = float(self.ui.conversion_input_theta.text().replace(',', '.'))
            qz = float(self.ui.conversion_input_qz.text().replace(',', '.'))

            lamb = float(self.ui.lineEdit_wavelength.text().replace(',', '.'))

        except BaseException as e:
            theta = 0
            qz = 0
            lamb = 1.54

        try:
            if self.ui.conversion_to_qz.isChecked():
                qz = 4 * math.pi / lamb * math.sin(math.radians(theta))
                self.ui.conversion_input_qz.setText("{:.8f}".format(qz))
            else:
                theta = math.degrees(math.asin(qz * lamb / (4 * math.pi))) % 360.0
                self.ui.conversion_input_theta.setText("{:.8f}".format(theta))

        except BaseException as e:
            print(e)
