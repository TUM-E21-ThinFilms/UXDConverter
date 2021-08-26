import numpy as np

from lxml import etree
from uxdconverter.measurement import MeasurementContext, Measurements, Measurement

AXIS_2THETA = '2Theta'
AXIS_OMEGA = 'Omega'
AXIS_PHI = 'Phi'
AXIS_CHI = 'Chi'
AXIS_Z = 'Z'
AXIS_X = 'X'
AXIS_Y = 'Y'

class XRDMLParser(object):
    def __init__(self, file_obj, logger):
        self._file = file_obj
        self._logger = logger

    def parse(self, context=None) -> Measurements:

        # use the default measurement context
        if context is None:
            context = MeasurementContext()

        try:
            tree = etree.parse(self._file)
            root = tree.getroot()
            mss = root.findall("xrdMeasurement", root.nsmap)
        except:
            raise RuntimeError("Could not read file %s" % self._file)

        # namespace
        namespace = root.nsmap

        if len(mss) > 1:
            raise RuntimeError("More than one xrdMeasurement entry?")

        ms = mss[0]
        measurements = self._get_measurements(ms, namespace)

        return Measurements([], measurements, [], context)


    def _get_measurements(self, xrd_entry, ns):
        return [self._get_measurement(scan, ns) for scan in xrd_entry.findall("scan", ns)]

    def _construct_measurement(self, theta, counts):
        dtheta = len(theta) * [0.0]
        dcounts = len(counts) * [0.0]
        data = np.array(list(zip(theta, dtheta, counts, dcounts)))

        return Measurement([], data)

    def _get_measurement(self, scan, ns):
        datapoints = scan.find("dataPoints", ns)

        counts = self._get_counts(datapoints, ns)
        len_counts = len(counts)
        theta = self._get_axis(AXIS_2THETA, datapoints, ns, len_counts) / 2.0
        omega = self._get_axis(AXIS_OMEGA, datapoints, ns, len_counts)
        z = self._get_axis(AXIS_Z, datapoints, ns, len_counts)

        measurement = self._construct_measurement(theta, counts)

        if omega is not None:
            # psi or omega_offset
            psi = - (theta - omega)
            measurement.set_psi(psi[0])

        return measurement

    def _find_axis(self, axis_name, datapoints, ns):
        for position in datapoints.findall("positions", ns):
            if position.get("axis") == axis_name:
                return position

        return None

    def _get_axis(self, axis_name, datapoints, ns, number_of_steps, type=float):
        axis = self._find_axis(axis_name, datapoints, ns)

        if axis is None:
            return None

        common_position = axis.find("commonPosition", ns)
        if common_position is not None:
            return type(common_position.text)

        list_position = axis.find("listPositions", ns)
        if list_position is not None:
            return np.array(list(map(type, list_position.text.split(" "))))

        start_position = axis.find("startPosition", ns)
        end_position = axis.find("endPosition", ns)
        if start_position is not None and end_position is not None:
            start = type(start_position.text)
            end = type(end_position.text)
            return np.linspace(start, end, number_of_steps)
        if start_position is not None or end_position is not None:
            raise RuntimeError("Only found startPosition or endPosition, but not both")

        return None

    def _get_counts(self, datapoints, ns):
        element = datapoints.find("counts", ns)

        if element is None:
            raise RuntimeError("datapoint entry did not contain counts")

        counts = np.array(list(map(int, element.text.split(" "))))

        return counts