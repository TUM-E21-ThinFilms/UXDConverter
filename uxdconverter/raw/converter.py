from uxdconverter.measurement import Measurement, Measurements as UXDMeasurements, MeasurementContext
from uxdconverter.raw.measurement import MeasurementRange, Measurements
from uxdconverter.raw.parser import RawParser
import numpy as np

class MeasurementConverter(object):
    def __init__(self):
        pass

    def convert(self, measurement: MeasurementRange):
        stepsize = measurement.get_header().get_step_size()
        steptime = measurement.get_header().get_step_time()
        start = measurement.get_header().get_start_theta()

        # Convert to counts per second
        data_y = np.array(measurement.get_data().get_data_points()) / steptime
        data_x = np.array(range(0, measurement.get_header().get_number_of_data_records())) * stepsize + start
        error_y = np.sqrt(data_y)

        # we do not care about headers at this point
        return Measurement([], [list(a) for a in zip(data_x, data_y, error_y)])


class MeasurementsConverter(object):
    def __init__(self):
        self.converter = MeasurementConverter()

    def convert_from_file(self, file):
        return self.convert(RawParser().parse_from_file(file))

    def convert(self, measurements: Measurements):
        converted = []

        for ms in measurements.get_measurements():
            converted.append(self.converter.convert(ms))

        return UXDMeasurements([], converted, [], MeasurementContext())

class RawMeasurementsParser(object):
    def __init__(self, file, logger):
        self._file = file
        self._logger = logger
        self._converter = MeasurementsConverter()

    def parse(self):
        try:
            f = open(self._file, "rb")
        except:
            raise RuntimeError("Could not open file %s" % self._file)

        return self._converter.convert(RawParser().parse(f.read()))



