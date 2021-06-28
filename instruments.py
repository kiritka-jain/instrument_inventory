from instrument_specification import InstrumentSpecifications


class Instrument:
    def __init__(self, serial_number: str, price: float, specs: InstrumentSpecifications):
        self.serial_number = serial_number
        self.price = price
        self.specs = specs

    def get_serial_number(self):
        return self.serial_number

    def get_price(self):
        return self.price

    def set_price(self, price_given):
        self.price = price_given

    def to_dict(self):
        result = {}
        result['serial_number'] = self.get_serial_number()
        result['price'] = self.get_price()
        result['specs'] = self.get_specs().to_dict()
        return result

    def get_specs(self):
        return self.specs





