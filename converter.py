import numpy as np
import os
import glob
import argparse
import logging
import matplotlib.pyplot as plt


class MeasurementContext(object):
    def __init__(self):
        self.sample_length = 10  # unit: mm
        self.wavelength = 1.5418  # unit: Angstroem
        self.xray_width = 0.1  # unit: mm
        self.saturation_threshold = 3.5e5  # unit: None
        self.knife_edge = False  # Whether or not the measurement was carried out with a knife edge.
        self.average_overlapping = False
        self.normalization = None
        # If a knife edge was used, no illumination correction is done.


class Measurement(object):
    def __init__(self, headers, data):
        self._headers = headers
        self._data = np.array(data)

    def get_data(self):
        return self._data

    def get_headers(self):
        return self._headers

    def get_data_region_x(self):
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
        measurements = [[]]

        measurement_number = 0

        self._file.seek(0)

        for line in self._file:
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
                parsed_data.append([float(ttheta) / 2.0, float(cps), 0.0])
            except:
                self._logger.error("Could not parse data line '%s'")

        return np.array(parsed_data)

    def parse(self, raw):
        raw_header, raw_data = self._split_measurement_from_header(raw)

        return Measurement(self._parse_header(raw_header), self._parse_data(raw_data))


def overlap_limits(measurement_1, measurement_2):
    """
    This method finds the x-value overlap of two measurements.
    This should be a symmetric function, i.e. overlap_limits(x, y) = overlap_limits(y, x)
    If one interprets the measurements as sets, then this method finds the intersection of them.

    :param Measurement measurement_1:
    :param Measurement measurement_2:
    :return: Tuple of x-values. (x_max, x_min) with x_max > x_min
    """

    data_1 = measurement_1.get_data()
    data_2 = measurement_2.get_data()

    # Compute the max's and min's for the x- values
    maxs = [np.amax(data_1, axis=0)[0], np.amax(data_2, axis=0)[0]]
    mins = [np.amin(data_1, axis=0)[0], np.amin(data_2, axis=0)[0]]

    overlap_max = min(maxs)
    overlap_min = max(mins)

    if overlap_max < overlap_min:
        raise ValueError("No overlap of the measurements found")

    return overlap_max, overlap_min


def merge_region(measurement_1, measurement_2):
    """
    This methods finds the 'merging region', i.e. the region where we have data points
    either from measurement_1, or from measurement_2.
    If one interprets the measurements as sets, then this corresponds to the union of them.

    :param Measurement measurement_1:
    :param Measurement measurement_2:
    :return:
    """

    data_1 = measurement_1.get_data()
    data_2 = measurement_2.get_data()

    maxs = [np.amax(data_1, axis=0)[0], np.amax(data_2, axis=0)[0]]
    mins = [np.amin(data_1, axis=0)[0], np.amin(data_2, axis=0)[0]]

    return max(maxs), min(mins)


def sort(measurement_1, measurement_2):
    """
    Sorts the measurements according to their x-value regions.
    Returns two measurements (ms_1, ms_2) such that the x-values of ms_1 <= ms_2

    :param Measurement measurement_1:
    :param Measurement measurement_2:
    :return:
    """

    data_1 = measurement_1.get_data()
    data_2 = measurement_2.get_data()

    maxs = [np.amax(data_1, axis=0)[0], np.amax(data_2, axis=0)[0]]

    if maxs[0] <= maxs[1]:
        return measurement_1, measurement_2
    else:
        return measurement_2, measurement_1


def overlapping_data(measurement_1, measurement_2, overlapping_region=None):
    """
    Returns the overlapping data from the two measurements.
    It computes the overlapping region, see overlap_limits and extracts the data which lies in this region

    A custom region can be passed via the overlapping_region parameter.

    :param Measurement measurement_1:
    :param Measurement measurement_2:
    :param tuple overlapping_region: First entry contains max limit, second one the min limit
    :return:
    """
    if overlapping_region is None:
        overlapping_region = overlap_limits(measurement_1, measurement_2)

    overlap_data_1 = np.array(
        [x for x in measurement_1.get_data() if (overlapping_region[0] >= x[0] >= overlapping_region[1])])
    overlap_data_2 = np.array(
        [x for x in measurement_2.get_data() if (overlapping_region[0] >= x[0] >= overlapping_region[1])])

    return overlap_data_1, overlap_data_2


def merge(measurement_1, measurement_2, scaling_factor=None, averaging=False):
    """
     This function merges two measurements. The merging is done in such a way,
     that at the overlap of the two measurements a scaling factor is computed.
     Then, we assume that at the overlap region, the measurements are identical (after a scaling)
     and thus we just take one of the measurements in the overlap region.
     At the other two regions, we just take one of the measurements (after a re-scaling).

     A user-defined scaling_factor can be passed by the argument.
     An averaging function at the overlap region can be performed by the averaging=True parameter.

     Note:
     The scaling factor is calculated to be bigger than 1 and is chosen to minimize the following problem:

     min_{alpha > 0} || f - \alpha g ||^2 = min_{\alpha > 0} \sum_{i=1}^{n} | f(x_i) - \alpha g(x_i) | ^2

     The solution to this problem is \alpha = (\sum f(x_i)) / (\sum g(x_i)) if f >= g. Otherwise switch f with g.

    :param Measurement measurement_1: First measurement
    :param Measurement measurement_2: Second measurement
    :param float scaling_factor: If None, the scaling_factor will be calculated by the formula above
    :param bool averaging: If True, in the overlapping region, the two measurements are averaged
    :return Measurement:
    """

    # first sort them, such that measurement_1 contains the data for the 'left' region
    # and measurement_2 contains the data for the 'right' region.
    measurement_1, measurement_2 = sort(measurement_1, measurement_2)

    # find out the region where they overlap
    overlap_region = overlap_limits(measurement_1, measurement_2)
    # and get the data in the overlapping region
    overlap_data_1, overlap_data_2 = overlapping_data(measurement_1, measurement_2, overlap_region)

    # We now assume that the x-values are correctly ordered,
    # i.e. the x-values are decreasing.

    # Next we want to compare at the same x-values. For that we just check for the
    # same amount of elements in the list. This should be enough.
    if not len(overlap_data_1) == len(overlap_data_2):
        raise ValueError("Cannot merge data sets, if the overlapping region has not the same data elements.")

    # Compute the scaling factor if the user did not specify it.
    if scaling_factor is None:
        # scaling_factor = np.average([overlap_data_1[i][1] / overlap_data_2[i][1] for i in range(len(overlap_data_1))])
        scaling_factor = sum([x[1] for x in overlap_data_1]) / sum([x[1] for x in overlap_data_2])
        if scaling_factor < 1:
            scaling_factor = 1 / scaling_factor

    # figure out, which measurement has bigger values in the overlapping region
    # then we scale the other measurement.
    diff = 0
    for i in range(len(overlap_data_1)):
        diff += (overlap_data_1[i][1] - overlap_data_2[i][1])

    # Already calculate the left and right data regions. They need to be scaled in the next step.
    data_left = np.array([x for x in measurement_1.get_data() if x[0] < overlap_region[1]])
    data_right = np.array([x for x in measurement_2.get_data() if x[0] > overlap_region[0]])

    if len(data_right) == 0:
        data_right = [[0, 0, 0]]

    if len(data_left) == 0:
        data_left = [[0, 0, 0]]

    scaling_array = np.array([1, scaling_factor, 1])

    if diff >= 0:
        # measurement_1 is bigger, hence scale measurement 2
        data_right = data_right * scaling_array
        overlap_data_2 = overlap_data_2 * scaling_array
    else:
        data_left = data_left * scaling_array
        overlap_data_1 = overlap_data_1 * scaling_array

    # Now we can perform the merging :)
    # The left region comes from measurement_1
    # The right region from measurement_2 (scaled)
    # The overlapping region either from measurement_1 or from the average of both
    if averaging is True:
        # now average over the two data sets
        data_middle = np.array(0.5 * (overlap_data_2 + overlap_data_1))
    else:
        # as the middle part, take the measurements which were not scaled.
        if diff >= 0:
            data_middle = np.array(overlap_data_1)
        else:
            data_middle = np.array(overlap_data_2)

    return Measurement(measurement_1.get_headers(), np.concatenate((data_left, data_middle, data_right)))


def subtract(measurement_1, measurement_2):
    """
     Calculates measurement_1 - measurement_2.
     This can only carried out in the overlapping region. Since, this is only used for subtracting the background
     from the measurement, the overlapping region is the whole data region. Nevertheless, we check that and print an
     error if this is not the case.
     The returned Measurement will only contain the overlapping region, the rest is thrown away.

    :param Measurement measurement_1:
    :param Measurement measurement_2:
    :return: A new measurement which is the difference of measurement_1 with measurement_2
    """

    overlap_data_1, overlap_data_2 = overlapping_data(measurement_1, measurement_2)

    if not len(overlap_data_1) == len(measurement_1.get_data()):
        print("Subtracting measurements: The overlapping region is smaller than before. Ignoring entries...")

    if not len(overlap_data_1) == len(overlap_data_2):
        raise ValueError(
            "Cannot subtract measurements, if the overlapping region does not contains the same amount of elements")

    # little trick, the minuend is just [0, -cps, 0] ;)
    data = overlap_data_1 - (overlap_data_2 * [0, 1, 0])
    return Measurement(measurement_1.get_headers(), data)


def calculate_errors(measurement):
    """
     Simply calculate the relative error. For poisson distributed data,
     the absolute error is \sqrt(y) where y is the measurement counts.
     The relative error is hence 1/\sqrt(y).

    :param Measurement measurement:
    :return:
    """

    data = [[x[0], x[1], 1 / np.sqrt(x[1])] for x in measurement.get_data()]
    return Measurement(measurement.get_headers(), data)


def perform_illumination_correction(measurement, context):
    """
        This method takes the measurement data and applies a illumination correction.

        When measuring samples without a knife edge, it happens that for smal angles, the footprint of the
        x-ray beam is bigger than the sample itself. Hence, we scale the reflected x-rays with the propotion of the
        footprint and the sample size.

        The footprint of the x-ray beam can be calculated as :
            w / \sin(\theta)
        with w being the x-ray beam width, \theta the angle between the incidence beam and the sample plane.

        Hence the scaling factor is w/(l * \sin(\theta) )
        with l beeing the sample size.

        Note that the scaling factor is only applied if the x-ray footprint is larger than the sample size, i.e.
            w / \sin(\theta) > l  <=> \theta <= \arcsin( w / l ) =: \theta_c

    :param Measurement measurement: the measurement to correct
    :param MeasurementContext context: the context of the measurement (needed for e.g. xray width and sample length)
    :return: Performs a new measurement with illumination correction applied
    """

    w = context.xray_width
    l = context.sample_length

    # in the docstring, \theta_c denoted, in degree
    critical_angle = np.arcsin(w / l) * 180 / np.pi
    # make a copy of the data, so we do not modify the data from the measurement (i.e. measurement is immutable)
    data = list(measurement.get_data())

    pre_scaling = float(w) / l

    # Correct the data
    for i in range(len(data)):
        # Correct only if the footprint is larger than the sample
        # So, scale the cps and the relative error
        if data[i][0] <= critical_angle:
            correction = pre_scaling / np.sin(data[i][0] * np.pi / 180)
            data[i][1] = data[i][1] * correction
            data[i][2] = data[i][2] * correction

    return Measurement(measurement.get_headers(), data)


def convert_to_qz(measurement, context):
    """
    Converts the x-data of measurement into qz data by the formula
        q_z = 4 * pi / \lambda * \sin(\theta)
    where \lambda is the wavelength to the x-ray beam and \theta is the reflectance angle.

    :param Measurement measurement:
    :param MeasurementContext context:
    :return Measurement:
    """

    # this is the constant pre-factor for the conversion
    # 4 * pi / \lambda
    pre_factor = 4 * np.pi / context.wavelength

    # make a copy
    data = list(measurement.get_data())

    for i in range(len(data)):
        data[i][0] = pre_factor * np.sin(data[i][0] * np.pi / 180)

    return Measurement(measurement.get_headers(), data)


def multi_merge(measurements, context):
    """
    Merges a list of measurements together into one

    :param list(Measurement) measurements:
    :return Measurement:
    """

    measurement = measurements[0]

    if len(measurements) > 1:
        # merge all measurements together
        merged = measurement
        for i in range(len(measurements) - 1):
            merged = merge(merged, measurements[i + 1], averaging=context.average_overlapping)

        measurement = merged

    return measurement


def convert_measurement(measurements):
    """
    Converts the measurements into a single measurement, by merging, subtracting and correcting the measurements in
    a reasonable manner:
        If there is just one measurement, a correction and normalization is done.
        If there are more than one measurements, the last measurement is considered as background, and the rest are
            normal 'locked coupled' measurements. Hence the 'locked coupled' are merged together, then the background
            is subtracted and after that, the correction and normalization is done.
        At the end, the measurement is converted to q_z values.

    :param Measurements measurements:
    :return Measurement:
    """

    mss = measurements.get_measurements()
    backgrounds = measurements.get_background_measurements()
    context = measurements.get_context()

    # default measurement.
    if len(mss) == 0:
        raise ValueError("Cannot convert if no measurement was given.")

    measurement = multi_merge(mss, context)

    # If we have any background, subtract it from the measurement
    if len(backgrounds) > 0:
        background = multi_merge(backgrounds, context)

        # Do the subtraction: measurement - background
        measurement = subtract(measurement, background)

    measurement = calculate_errors(measurement)

    if context.knife_edge is False:
        measurement = perform_illumination_correction(measurement, context)

    measurement = normalize(measurement, context.normalization)

    measurement = convert_to_qz(measurement, context)
    return measurement


def export_to_dat(measurement, file):
    """
    Exports a measurement to a file.
    The format is readable by Parratt-Software

    :param Measurement measurement:
    :param str file:
    :return:
    """

    fp = open(file, 'w')
    data = measurement.get_data()

    # write out at most 1000 lines. Parratt cannot handle more than that...
    for idx in range(min(len(data), 999)):
        x = "{:.3E}".format(data[idx][0])
        y = "{:.3E}".format(data[idx][1])
        err_y = "{:.3E}".format(data[idx][2])

        line = "\t".join([x, y, err_y]) + "\n"

        fp.write(line)

    fp.close()


def normalize(measurement, method='max'):
    """
    Normalizes the measurement to one.

    Available methods:
        'max': Normalizes the maximum count to 1.
        'flank': Find the first flank of the reflectivity curve, and then normalizes the point with the lowest
                    absolute slope to 1.

    Normalizing is applied to the whole data set and done by scaling the y values and errors (i.e. counts).

    :param Measurement measurement:
    :param method: supported methods are: 'max', 'flank'
    :return:
    """
    if method is None:
        method = 'flank'

    if method == 'max':
        """
         Just find the point with the most counts per second, and normalize this point to 1. The scaling factor is 
         applied to every point.
        """
        data = list(measurement.get_data())
        max = np.amax([x[1] for x in data])
        norm = 1.0 / max
        return Measurement(measurement.get_headers(), data * np.array([1, norm, norm]))

    if method == 'flank':
        """
         First find the first flank (i.e. the point with the smallest derivative (the point where the graph's gradient 
         has the greatest descending. Then look for the points left to it (this should then be the region of total
         reflection) and find there the point with the slope nearest to zero, i.e. with the smallest absolute gradient.
        """

        data = list(measurement.get_data())
        # Find the first flank via the gradient.
        deriv = np.gradient([x[1] for x in data], [x[0] for x in data])
        first_flank = np.argmin(deriv)

        # Now look at the points left to the first flank, and find the smalles absolute slope.
        vf = np.vectorize(abs)
        left_deriv = vf(deriv[0:first_flank])
        idx = np.argmin(left_deriv)

        # The scaling factor is then 1 / y_c, where y_c is the point with the lowest absolute slope
        norm = 1.0 / data[idx][1]
        return Measurement(measurement.get_headers(), data * np.array([1, norm, norm]))

    if isinstance(method, float):
        data = measurement.get_data()
        return Measurement(measurement.get_headers(), data * np.array([1, method, method]))


def plot(measurement, names=None):
    """
    Plots the measurement.

    If measurement is of type list, earch measurement in the list is plotted in the same graph.


    :param Measurement measurement: Single measurement or a list if measurements.
    :return: None
    """
    if not isinstance(measurement, list):
        measurement = [measurement]

    if not names is None and not len(names) == len(measurement):
        raise ValueError("Given names must have the same length as measurements")
    handles = []
    for ms in measurement:
        data = ms.get_data()
        x = [x[0] for x in data]
        y = [x[1] for x in data]
        y_err = [x[2] for x in data]

        handles.append(plt.errorbar(x, y, yerr=y_err))

    if not names is None:
        plt.legend(handles, names)

    plt.yscale('log')
    plt.show()


def interactive_plot(measurement):
    data = measurement.get_data()

    x = [x[0] for x in data]
    y = [x[1] for x in data]
    global picked, norm
    picked = []
    norm = None

    plt.plot   (x, y)
    plt.yscale('log')
    # plt.show()

    def on_click(event):
        global picked
        if event.button == 1:
            if event.inaxes:
                print('Picked coords %f %f' % (event.xdata, event.ydata))
                picked.append((event.xdata, event.ydata))

    def on_keyboard(event):
        global picked, norm
        if event.key == 'x' and len(picked) > 0:
            norm = picked[-1]
            picked = []


    plt.gcf().canvas.mpl_connect('button_press_event', on_click)
    plt.gcf().canvas.mpl_connect('key_press_event', on_keyboard)
    plt.show()

    return norm



def get_logger(name):
    """
    Creates a logger with given name
    :param str name:
    :return: logging object
    """
    logger = logging.getLogger(name)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


def main():
    parser = argparse.ArgumentParser(description='Process input directory to convert .UXD files to .dat files')
    parser.add_argument('-d', '--directory', type=str, nargs='?', help='directory to search for .UXD files',
                        default=os.getcwd())
    parser.add_argument('-f', '--file', type=str, nargs='?', help='a file to convert .UXD to .dat', default=None)
    parser.add_argument('-v', '--verbose', type=bool, nargs='?', help='print logging messages', default=False)
    args = parser.parse_args()
    path = args.directory
    file = args.file
    verbose = args.verbose

    logger = get_logger(__name__)
    if verbose:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.WARNING)

    if file is not None:
        files = [file]
    else:
        files = glob.glob(path + "/*.UXD")

    if len(files) == 0:
        raise ValueError("No .uxd files found")

    output_path = os.path.dirname(os.path.realpath(files[0])) + "/dat/"
    try:
        if not os.path.exists(output_path):
            os.mkdir(output_path)
    except:
        logger.warning('Exception while creating path %s', output_path)
        pass

    for file in files:
        output_name = output_path + os.path.basename(file).replace("UXD", "dat")
        logger.info("Converting file %s to %s ...", file, output_name)
        mss = MeasurementsParser(open(file, 'r'), logger).parse()
        ms = convert_measurement(mss)
        export_to_dat(ms, output_name)

        plot(ms)

    return 0


if __name__ == '__main__':
    main()
