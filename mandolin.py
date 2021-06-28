from instruments import Instrument
from mandolin_specs import MandolinSpecs


class Mandolin(Instrument):
    def __init__(self, serial_number: str, price: float, specs: MandolinSpecs):
        Instrument.__init__(self, serial_number, price, specs)

