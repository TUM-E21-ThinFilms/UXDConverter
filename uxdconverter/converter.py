"""import os
import glob
import argparse
import logging

from uxdconverter.parser import MeasurementsParser
"""

from uxdconverter.measurement import Measurements, Measurement
from uxdconverter.operation import MultiMerger, MeasurementMerger, MeasurementSubtraction, DataIlluminationCorrection, \
    DataNormalization, QzCalculation, QzCropping


class Converter(object):
    def __init__(self, measurements: Measurements):
        self._backgrounds = measurements.get_background_measurements()
        self._context = measurements.get_context()
        self._measurements = measurements.get_measurements()

        self._multi_merge = MultiMerger(MeasurementMerger())
        self._subtract = MeasurementSubtraction()
        self._illumination = DataIlluminationCorrection()
        self._normalization = DataNormalization()
        self._qz_calc = QzCalculation()
        self._cropping = QzCropping()

    def convert(self) -> Measurement:
        """
        Converts the measurements into a single measurement, by merging, subtracting and correcting the measurements in
        a reasonable manner:
            If there is just one measurement, a correction and normalization is done.
            If there are more than one measurements, the last measurement is considered as background, and the rest are
                normal 'locked coupled' measurements. Hence the 'locked coupled' are merged together, then the background
                is subtracted and after that, the correction and normalization is done.
            At the end, the measurement is converted to q_z values.

        :return Measurement:
        """

        mss = self._measurements
        backgrounds = self._backgrounds
        context = self._context

        # default measurement.
        if len(mss) == 0:
            raise ValueError("Cannot convert if no measurement was given.")

        measurement = self._multi_merge.merge(mss)

        # If we have any background, subtract it from the measurement
        if len(backgrounds) > 0:
            background = self._multi_merge.merge(backgrounds)

            # Do the subtraction: measurement - background
            measurement = self._subtract.subtract(measurement, background)

        if context.knife_edge is False:
            measurement = self._illumination.manipulate(measurement, context)

        measurement = self._normalization.manipulate(measurement, context)

        if self._context.qz_conversion is True:
            measurement = self._qz_calc.manipulate(measurement, context)

        measurement = self._cropping.manipulate(measurement, context)

        return measurement


"""
def get_logger(name):
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

        plot([ms])

    return 0


if __name__ == '__main__':
    main()
"""