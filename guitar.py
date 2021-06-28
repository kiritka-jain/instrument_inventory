from guitar_specs import GuitarSpecs
from instruments import Instrument


class Guitar(Instrument):
    def __init__(self, serial_number: str, price: float, specs: GuitarSpecs):
        Instrument.__init__(self, serial_number, price, specs)
