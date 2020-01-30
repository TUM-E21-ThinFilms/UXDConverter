import numpy as np
import codecs
from uxdconverter.measurement import MeasurementContext, Measurement, Measurements

class MeasurementsParser(object):
    def __init__(self, file_obj, logger):
        self._file = file_obj
        self._logger = logger

    def _read_measurements(self):

        # Contains as the first element the general header information
        # Then, for every positive index, the array contains headers and
        # the measurement data. The headers differ for each measurement.

        # i.e.
        # measurements = [general_header, header_and_measurement_1, header_and_measurement_2, ... header_and_measurement_n]

        try:
            file = codecs.open(self._file, 'r', encoding='utf-8', errors='ignore')
        except:
            raise RuntimeError("Could not open file %s" % self._file)



        measurements = [[]]

        measurement_number = 0

        file.seek(0)

        for line in file:
            # This is the mark for a data set with headers. After this mark,
            # a few headers (context data) for a measurement and the measurement itself
            # is located
            if line.startswith('; (Data for Range number'):
                measurement_number += 1
                measurements.append([])

            measurements[measurement_number].append(line)

        return measurements

    def parse(self, context=None):

        # use the default measurement context
        if context is None:
            context = MeasurementContext()

        ms_parser = MeasurementParser(self._logger)

        measurements = self._read_measurements()

        if len(measurements) < 2:
            self._logger.error("Did not found any measurements")

        raw_header = measurements.pop(0)
        header = ms_parser.parse_header(raw_header)

        parsed_measurements = []
        parsed_backgrounds = []

        for measurement in measurements:
            parsed_measurements.append(ms_parser.parse(measurement))

        if len(parsed_measurements) > 1:
            parsed_backgrounds.append(parsed_measurements.pop())

        return Measurements(header, parsed_measurements, parsed_backgrounds, context)


class MeasurementParser(object):
    def __init__(self, logger):
        self._logger = logger

    def _split_measurement_from_header(self, raw):

        header = []
        data = []

        in_header = True

        for line in raw:
            # This header indicates the start of the data section
            if line.startswith('_2THETACPS'):
                in_header = False
                continue

            if in_header:
                header.append(line)
            else:
                data.append(line)

        return header, data

    def parse_header(self, raw):
        return self._parse_header(raw)

    def _parse_header(self, raw):
        parsed_headers = {}

        for header in raw:
            # we ignore this, since this is not really a header
            # but just a section indicator
            if header.startswith(';'):
                continue

            # looks like a good header
            if header.startswith('_'):
                try:
                    key, value = header.split('=')
                    # remove the leading underscore
                    key = key[1:]

                    parsed_headers[key] = value
                except:
                    self._logger.warning("Could not parse header line '%s'")

        return parsed_headers

    def _parse_data(self, raw):
        parsed_data = []

        for line in raw:
            try:
                # every data line contains the 2theta and counts_per_second information. Nothing more, nothing less.
                ttheta, cps = line.replace(',', '.').split()
                # add 2theta, cps, and delta_cps, where delta_cps is currently set to zero.
                # divide 2theta by 2, so we just have theta :)
                parsed_data.append([float(ttheta) / 2.0, 0.0, float(cps), 0.0])
            except:
                self._logger.error("Could not parse data line '%s'")

        return np.array(parsed_data)

    def parse(self, raw):
        raw_header, raw_data = self._split_measurement_from_header(raw)

        return Measurement(self._parse_header(raw_header), self._parse_data(raw_data))

class SimpleMeasurementsParser(object):
    def __init__(self, file_obj, logger):
        self._file = file_obj
        self._logger = logger

    def parse(self, context=None):

        # use the default measurement context
        if context is None:
            context = MeasurementContext()

        # we assume that the file structure is readable by numpy.loadtxt
        # and the data format is:
        #
        # 2theta cps
        #
        # where 2theta is the 2 theta angle of incidence
        # and cps (counts per second) is the measured intensity
        data = np.loadtxt(self._file)

        parsed = []

        for key, entry in enumerate(data):
            if len(entry) > 1:
                parsed.append([float(entry[0]) / 2.0, 0.0, float(entry[1]), 0.0])
            else:
                self._logger.error("Could not parse data line '%s'", key)

        parsed = np.array(parsed)

        # we have no headers here...
        measurement = Measurement([], parsed)

        # also, we have no headers here and no background.
        return Measurements([], [measurement], [], context)