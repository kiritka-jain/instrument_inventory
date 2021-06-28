from instrument_inventory.enum_instrument import Builder, Type, Wood, Style
from instrument_inventory.instrument_specification import InstrumentSpecifications


class MandolinSpecs(InstrumentSpecifications):
    def __init__(self, builder: Builder, model: str, type: Type, backwood: Wood, topwood: Wood, style: Style):
        super().__init__(builder, model, type, backwood, topwood)
        self.style = style

    def get_style(self):
        return self.style

    def compare(self, other_specs):
        return super().compare(other_specs) and other_specs.style == self.style
