from enum_instrument import Builder, Type, Wood


class InstrumentSpecifications:
    def __init__(self, builder: Builder, model: str, type: Type, backwood: Wood, topwood: Wood):
        self.builder = builder
        self.model = model
        self.type = type
        self.backwood = backwood
        self.topwood = topwood

    def get_builder(self):
        return self.builder

    def get_model(self):
        return self.model

    def get_type(self):
        return self.type

    def get_backwood(self):
        return self.backwood

    def get_topwood(self):
        return self.topwood

    def compare(self, other_specs):
        if other_specs.type != self.type:
            return False
        if other_specs.model != self.model:
            return False
        if other_specs.topwood != self.topwood:
            return False
        if other_specs.backwood != self.backwood:
            return False
        return True

    def to_dict(self):
        result = {}
        result['builder'] = self.get_builder()
        result['model'] = self.get_model()
        result['type'] = self.get_type()
        result['backwood'] = self.get_backwood()
        result['topwood'] = self.get_topwood()
        result['topwood'] = self.get_topwood()
        return result
