import os

from uxdconverter.parser.uxd import MeasurementsParser
from uxdconverter.parser.simple import SimpleMeasurementsParser
from uxdconverter.parser.raw import RawMeasurementsParser
from uxdconverter.parser.nicos import NicosParser

class GeneralParser(object):
    def __init__(self):
        pass

    def parse(self, file, logger):
        ext = os.path.splitext(file)[1]

        if ext.lower() == '.raw':
            return RawMeasurementsParser(file, logger).parse()
        elif ext.lower() == '.uxd':
            return MeasurementsParser(file, logger).parse()
        elif ext.lower() == '.dat':
            return NicosParser(file, logger).parse()
        else:
            return SimpleMeasurementsParser(file, logger).parse()
