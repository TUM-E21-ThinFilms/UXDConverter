import numpy as np


class MeasurementContext(object):
    def __init__(self):
        self.sample_length = 10  # unit: mm
        self.wavelength = 1.5418  # unit: Angstroem
        self.xray_width = 0.1  # unit: mm
        self.saturation_threshold = 3.5e5  # unit: None
        self.knife_edge = False  # Whether or not the measurement was carried out with a knife edge.
        self.average_overlapping = False  # If a knife edge was used, no illumination correction is done.
        self.normalization = None  # Type of normalization method.
        self.qz_range = (0, 1)
        self.qz_conversion = True


class Measurement(object):
    def __init__(self, headers, data):
        self._headers = headers
        self._data = np.array(data)
        self._remove_strange_data_points()

    def _remove_strange_data_points(self):
        """
        Removes "strange" data points, i.e. data points with counts less or equal to zero counts.

        :return:
        """
        data = self._data.T
        # Thats the counts.
        ind = data[1] > 0

        new_data = 3*[None]

        new_data[0] = data[0][ind]
        new_data[1] = data[1][ind]
        new_data[2] = data[2][ind]

        self._data = np.array(new_data).T

    def get_data(self):
        return np.copy(self._data)

    def scale_y(self, factor):
        self._data = self._data * np.array([1, factor, factor])

    def get_headers(self):
        return self._headers

    def get_data_region_x(self) -> (float, float):
        """
        Returns the data region for the x-variable (i.e. theta)
        :return: (max, min)
        """
        max = np.amax(self._data, axis=0)[0]
        min = np.amin(self._data, axis=0)[0]

        return max, min


class Measurements(object):
    def __init__(self, header, measurements, backgrounds, measurement_context):
        self._header = header
        self._measurement = measurements
        self._background_measurement = backgrounds
        self._measurement_context = measurement_context

    def get_headers(self):
        return self._header

    def set_context(self, context):
        self._measurement_context = context

    def get_context(self):
        """

        :return MeasurementContext:
        """
        return self._measurement_context

    def get_count_measurements(self):
        return len(self._measurement)

    def get_measurement(self, index):
        return self._measurement[index]

    def get_measurements(self):
        """

        :return list(Measurement):
        """
        return self._measurement

    def get_background_measurements(self):
        return self._background_measurement

    def add(self, mss: 'Measurements'):
        self._measurement = self._measurement + mss.get_measurements()
        self._background_measurement = self._background_measurement + mss.get_background_measurements()
