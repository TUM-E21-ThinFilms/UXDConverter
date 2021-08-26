import numpy as np

from periodictable.xsf import xray_sld, xray_wavelength
from periodictable.nsf import neutron_sld, neutron_scattering
from periodictable.formulas import formula

from uxdconverter.units.si import SI
from uxdconverter.units.wavelength import Wavelength

from uxdconverter.transition_energy.database import TransitionDatabase
from uxdconverter.ui.gui import Ui_UXDConverter

from uxdconverter.ui.util import hightlight

SI_PREFIX = {
    'M': 1e6,
    'k': 1e3,
    'd': 1e-1,
    'c': 1e-2,
    'm': 1e-3,
    'µ': 1e-6,
    'n': 1e-9,
    'p': 1e-12,
    'f': 1e-15,
}

EMISSON_LINES = {
    'Ka1': 'KL3',
    'Ka2': 'KL2',
    'Kb': 'KM3',
    # Ka has to be the last element, as we iterate through it and it conflicts with Ka1
    'Ka': 'KL3',
}


class SldTabController(object):
    def __init__(self, ui: Ui_UXDConverter, app, trans_db: TransitionDatabase):
        self.ui = ui
        self._app = app
        self._trans_db = trans_db

        self.setup()

    def _r(self, f):
        r = lambda x: round(x, 6)
        if isinstance(f, list) or isinstance(f, tuple):
            return [r(fs) for fs in f]

        return r(f)

    def setup(self):
        self.ui.btn_SLD_calculate.clicked.connect(self.calculate)

    def _log_ex(self, exception):
        print(exception)

    def calculate(self):
        compound = self.get_compound()
        wavelength_n = self.get_neutron_wavelength()
        wavelength_x = self.get_xray_wavelength()
        thickness = self.get_thickness()

        if compound is None or compound.density is None or wavelength_x is None or wavelength_n is None or thickness is None:
            return

        self.calculate_penetration_depth(compound, wavelength_n, wavelength_x, thickness)
        self.calculate_sld(compound, wavelength_n, wavelength_x)

    def calculate_penetration_depth(self, compound, wavelength_n, wavelength_x, thickness):
        sld, xs, pendepth = neutron_scattering(compound, density=compound.density, wavelength=wavelength_n)
        sld_x_real, sld_x_imag = xray_sld(compound, density=compound.density, wavelength=wavelength_x)

        xs_coh, xs_abs, xs_incoh = xs
        p_abs, p_abs_incoh, p_abs_incoh_coh = [1 / xs_abs, 1/(xs_abs+xs_incoh), 1 / (xs_abs+xs_coh+xs_incoh)]
        p_abs_r, p_abs_incoh_r, p_abs_incoh_coh_r = self._r([p_abs, p_abs_incoh, p_abs_incoh_coh])

        # not 100% sure about the 1/2...
        p_abs_xray = 1 / (2 * wavelength_x * sld_x_imag * 1e-6) * 1e-4

        tr_att = lambda d, pen: (np.exp(-d / pen) * 100, np.exp(d / pen))
        # thickness is in [m], p_abs_incoh in [cm], thus 1e-2
        tr_n, att_n = tr_att(thickness, p_abs_incoh * 1e-2)
        # p_abs_xray in [µm], thus 1e-6
        tr_x, att_x = tr_att(thickness, p_abs_xray * 1e-6)

        self.ui.lE_SLD_pendepth_neutron_abs.setText(f"{p_abs_r}")
        self.ui.lE_SLD_pendepth_neutron_abs_incoh.setText(f"{p_abs_incoh_r}")
        self.ui.lE_SLD_pendepth_neutron_abs_incoh_coh.setText(f"{p_abs_incoh_coh_r}")
        self.ui.lE_SLD_pendepth_neutron_transmission.setText(f"{tr_n} %")
        self.ui.lE_SLD_pendepth_neutron_attenuation.setText(f"{att_n}")

        self.ui.lE_SLD_pendepth_xray_abs.setText(f"{self._r(p_abs_xray)}")
        self.ui.lE_SLD_pendepth_xray_transmission.setText(f"{tr_x} %")
        self.ui.lE_SLD_pendepth_xray_attenuation.setText(f"{att_x}")

    def calculate_sld(self, compound, neutron_wavelength, xray_wavelength):
        wavelength_n = neutron_wavelength
        wavelength_x = xray_wavelength
        density = compound.density

        n_real, n_imag, n_incoh = self._r(neutron_sld(compound, density=density, wavelength=wavelength_n))
        x_real, x_imag = self._r(xray_sld(compound, density=density, wavelength=wavelength_x))

        self.ui.lE_SLD_neutron_real.setText(f"{n_real}")
        self.ui.lE_SLD_neutron_imag.setText(f"{n_imag}")
        self.ui.lE_SLD_neutron_incoh.setText(f"{n_incoh}")

        self.ui.lE_SLD_xray_real.setText(f"{x_real}")
        self.ui.lE_SLD_xray_imag.setText(f"{x_imag}")

    def get_neutron_wavelength(self):
        """
        Returns the neutron wavelength in [AA]
        :return:
        """
        wavelength_str = self.ui.lE_source_neutron.text()
        try:
            wavelength = float(wavelength_str.replace('AA', '').replace('Ang', ''))
            if wavelength > 0:
                return wavelength
        except BaseException as e:
            hightlight(self.ui.lE_source_neutron)
            self._log_ex(e)

        return None

    def get_xray_wavelength(self):
        """
        Returns the xray wavelength in [AA]
        :return:
        """



        wavelength_str = self.ui.lE_source_xray.text()
        try:
            return Wavelength.from_string(wavelength_str, self._trans_db)
        except Exception as e:
            self._log_ex(e)
            hightlight(self.ui.lE_source_xray)
            return None

        # TODO: use wavelength class
        try:
            if np.any([emisson_line in wavelength_str for emisson_line in EMISSON_LINES.keys()]):
                for emisson_line in EMISSON_LINES.keys():
                    if not emisson_line in wavelength_str:
                        continue

                    element = wavelength_str.replace(emisson_line, '').strip()
                    transitions = self._trans_db.get_all_transitions(element, EMISSON_LINES[emisson_line])
                    if len(transitions) != 1:
                        hightlight(self.ui.lE_source_xray)
                        return None
                    # transition db returns in eV, xray-wavelength expects keV
                    return xray_wavelength(transitions[EMISSON_LINES[emisson_line]]['experimental'] * 1e-3)
        except BaseException as e:
            self._log_ex(e)
            hightlight(self.ui.lE_source_xray)
            return None

        try:
            wavelength = float(wavelength_str.replace('AA', '').replace('Ang', ''))
            if wavelength > 0:
                return wavelength
        except BaseException as e:
            hightlight(self.ui.lE_source_xray)
            self._log_ex(e)

        # Cu Ka wavelength
        return None

    def get_compound(self):
        compound_str = self.ui.lE_SLD_sample_material.text()
        density = self.get_density()

        if compound_str == "":
            hightlight(self.ui.lE_SLD_sample_material)
            return None

        return formula(compound_str, density=density)

    def get_density(self):
        density_str = self.ui.lE_SLD_sample_density.text()

        if density_str == '':
            return None

        try:
            return float(density_str)
        except BaseException as e:
            hightlight(self.ui.lE_SLD_sample_density)
            self._log_ex(e)
            return None

    def get_thickness(self):
        """
        Returns the thickness in [m]
        :return:
        """
        thickness_str = self.ui.lE_SLD_sample_thickness.text()
        if thickness_str == '':
            return 1e-2  # 1 cm is default

        try:
            return SI.extract_number(thickness_str, 'm')
        except Exception as e:
            self._log_ex(e)
            hightlight(self.ui.lE_SLD_sample_thickness)
            return None