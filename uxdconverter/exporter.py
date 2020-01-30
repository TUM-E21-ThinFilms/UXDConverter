import codecs
from uxdconverter.measurement import Measurement


class AbstractExportAlgorithm(object):
    EXPORT_MODE_Q = 0
    EXPORT_MODE_THETA = 1

    EXPORT_MODES = [EXPORT_MODE_Q, EXPORT_MODE_THETA]

    def __init__(self):
        self._mode = self.EXPORT_MODE_Q

    def export_mode(self, mode):
        if not mode in self.EXPORT_MODES:
            raise RuntimeError("Unknown export mode")

        self._mode = mode

    def export(self, measurement: Measurement) -> str:
        raise NotImplementedError()


class FileExporter(object):
    def __init__(self, output_file, export_algorithm: AbstractExportAlgorithm):
        self._file = output_file
        self._alg = export_algorithm

    def do_export(self, measurement: Measurement):
        fp = codecs.open(self._file, 'w')
        fp.write(self._alg.export(measurement))
        fp.close()


class ParrattExportAlgorithm(AbstractExportAlgorithm):

    def export(self, measurement: Measurement):

        if self._mode is self.EXPORT_MODE_THETA:
            header = ["# Theta [deg]: incident angle theta of x-rays",
                      "# dTheta [deg]: error in theta (absolute)",
                      "# R [1]: normalized reflectivity",
                      "# dR [1]: error in reflectivity (absolute)",
                      "# theta\tdTheta\tR\tdR",]

        elif self._mode is self.EXPORT_MODE_Q:
            header = ["# q_z [A^-1]: wavevector transfer in z direction",
                      "# dq [A^-1]: error in q (absolute)",
                      "# R [1]: normalized reflectivity",
                      "# dR [1]: error in reflectivity (absolute)",
                      "# q\tdq\tR\tdR", ]

        data_line = 999 * [""]

        data = measurement.get_data()

        # write out at most 1000 lines. Parratt cannot handle more than that...
        for idx in range(min(len(data), 999)):
            x = "{:.4E}".format(data[idx][0])
            err_x = "{:.4E}".format(data[idx][1])
            y = "{:.4E}".format(data[idx][2])
            err_y = "{:.4E}".format(data[idx][3])

            data_line[idx] = "\t".join([x, err_x, y, err_y])

        return "\n".join(header + data_line).strip()
