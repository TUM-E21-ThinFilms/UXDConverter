import math

from uxdconverter.ui.gui import Ui_UXDConverter

import math

CONST_H = 6.62607015e-34  # J s
CONST_HBAR = CONST_H / (2 * math.pi)  # J s
CONST_MASS_NEUTRON = 1.67492749804e-27  # kg
CONST_MASS_PROTON = 1.67262192369e-27  # kg
CONST_MASS_ELECTRON = 9.1093837015e-31  # kg
CONST_ELEMENTARY_CHARGE = 1.602176634e-19  # C
CONST_NUCLEAR_MAGNETON = CONST_ELEMENTARY_CHARGE * CONST_HBAR / 2 / CONST_MASS_PROTON  # J / T
CONST_MU_NEUTRON = -1.91304272 * CONST_NUCLEAR_MAGNETON
CONST_MU_BOHR = CONST_ELEMENTARY_CHARGE * CONST_HBAR / 2 / CONST_MASS_ELECTRON  # J / T


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


def mag_sld_to_mu_bohr(mag_sld):
    # mag_sld is given in 1/AA**2, so convert this to 1/m**2
    mag_sld = mag_sld * 1e20
    B = mag_sld * 2 * math.pi * CONST_HBAR ** 2 / (CONST_MASS_NEUTRON * CONST_MU_NEUTRON)
    return B
    # SLD_m = N * p
    # 2 pi hbar**2/ (m_n µ_n) * SLD_m = B
