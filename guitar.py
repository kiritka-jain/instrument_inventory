from instrument_inventory.guitar_specs import GuitarSpecs
from instrument_inventory.instruments import Instrument
from instrument_inventory.instrument_specification import InstrumentSpecifications


class Guitar(Instrument):
    def __init__(self, serial_number: str, price: float, specs: GuitarSpecs):
        Instrument.__init__(self, serial_number, price, specs)
