import matplotlib.pyplot as plt
from uxdconverter.ui.controller import Controller
from uxdconverter.diffraction.crystal import DiffractionContext, BraggCondition, CubicSpacing, InterplanarSpacing
from uxdconverter.converter import Converter

from enum import Enum

class SampleReference(Enum):
    NIST_LaB6 = 'LaB6 (660c)'
    NIST_Si   = 'Si (640f)'

    CRYSTAL_STRUCTURE = {
        NIST_LaB6: CubicSpacing({InterplanarSpacing.PARAMETER_A: 4.156826}),
        NIST_Si: CubicSpacing({InterplanarSpacing.PARAMETER_A: 5.431144})
    }

class ReferenceActionController(object):
    def __init__(self, controller: Controller):
        self.controller = controller
        self._int_spacing = None

    def set_reference(self, reference: SampleReference):
        self._ref = reference
        self._int_spacing = SampleReference.CRYSTAL_STRUCTURE.value[reference.value]

    def run(self):
        ctx = self.controller._settings_controller.get_measurement_context()
        ctx.qz_conversion = False
        theta_min, theta_max = ctx.qz_range

        diff_ctx = DiffractionContext()
        diff_ctx._wavelength = ctx.get_wavelength()

        if self._int_spacing is None:
            return

        bragg = BraggCondition(diff_ctx, self._int_spacing)
        hkl = bragg.get_all_hkl(theta_max)

        try:

            measurements = self.controller.setup_measurement()
            measurements.set_context(ctx)
            ms = Converter(measurements).convert()
        except BaseException as e:
            self.controller.logger.exception(e)
            return

        self._plot_peaks(bragg, hkl)
        self.controller._plotting.plot([ms], ctx)

    def _plot_peaks(self, bragg, hkls):
        thetas = []
        for hkl in hkls:
            h, k, l = hkl
            theta = bragg.get_theta(*hkl)
            if theta in thetas:
                continue
            plt.axvline(theta)
            plt.text(theta, 0, f"[{h} {k} {l}]", horizontalalignment='left')
            thetas.append(theta)


