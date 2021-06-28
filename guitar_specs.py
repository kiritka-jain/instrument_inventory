from enum_instrument import Builder, Type, Wood
from instrument_specification import InstrumentSpecifications


class GuitarSpecs(InstrumentSpecifications):
    def __init__(self, builder: Builder, model: str, type: Type, backwood: Wood, topwood: Wood, no_strings: int = 4):
        super().__init__(builder, model, type, backwood, topwood)
        self.no_strings = no_strings

    def get_no_strings(self):
        return self.no_strings

    def compare(self, other_specs):
        return other_specs.no_strings == self.no_strings and super().compare(other_specs)

