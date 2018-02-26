import codecs
from uxdconverter.measurement import Measurement


class AbstractExportAlgorithm(object):
    def __init__(self):
        pass

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

        data_line = 999 * [""]

        data = measurement.get_data()

        # write out at most 1000 lines. Parratt cannot handle more than that...
        for idx in range(min(len(data), 999)):
            x = "{:.3E}".format(data[idx][0])
            y = "{:.3E}".format(data[idx][1])
            err_y = "{:.3E}".format(data[idx][2])

            data_line[idx] = "\t".join([x, y, err_y])

        return "\n".join(data_line).strip()
