from instrument_inventory.enum_instrument import Style
from instrument_inventory.instruments import Instrument
from instrument_inventory.instrument_specification import InstrumentSpecifications
from instrument_inventory.mandolin_specs import MandolinSpecs


class Mandolin(Instrument):
    def __init__(self, serial_number: str, price: float, specs: MandolinSpecs):
        Instrument.__init__(self, serial_number, price, specs)

