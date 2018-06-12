import os

from uxdconverter.parser import MeasurementsParser
from uxdconverter.raw.converter import RawMeasurementsParser


class FileParser(object):
    def __init__(self):
        pass

    def parse(self, file, logger):
        ext = os.path.splitext(file)[1]

        if ext.lower() == '.raw':
            return RawMeasurementsParser(file, logger).parse()
        else:
            return MeasurementsParser(file, logger).parse()
