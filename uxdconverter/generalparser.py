import os

from uxdconverter.parser import MeasurementsParser, SimpleMeasurementsParser
from uxdconverter.raw.converter import RawMeasurementsParser


class FileParser(object):
    def __init__(self):
        pass

    def parse(self, file, logger):
        ext = os.path.splitext(file)[1]

        if ext.lower() == '.raw':
            return RawMeasurementsParser(file, logger).parse()
        elif ext.lower() == '.uxd':
            return MeasurementsParser(file, logger).parse()
        else:
            return SimpleMeasurementsParser(file, logger).parse()
