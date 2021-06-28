from typing import List

from instrument_specification import InstrumentSpecifications
from instruments import Instrument


class Inventory:
    def __init__(self):
        self.instruments = []

    def add_instrument(self, instrument: Instrument):
        self.instruments.append(instrument)

    def get_instrument(self, serial_number: str) -> Instrument:
        for instrument in self.instruments:
            if instrument.serial_number == serial_number:
                return instrument

    def search_instrument(self, specs: InstrumentSpecifications) -> List:
        matching_instruments = []
        for instrument in self.instruments:
            if isinstance(instrument.specs, type(specs)) and specs.compare(instrument.specs):
                matching_instruments.append(instrument)
        return matching_instruments
