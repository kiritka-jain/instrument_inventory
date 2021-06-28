from instrument_inventory.enum_instrument import Builder, Type, Wood, Style
from instrument_inventory.guitar import Guitar
from instrument_inventory.guitar_specs import GuitarSpecs
from instrument_inventory.mandolin import Mandolin
from instrument_inventory.instrument_specification import InstrumentSpecifications
from instrument_inventory.inventory import Inventory
from instrument_inventory.mandolin_specs import MandolinSpecs

specification_1 = GuitarSpecs(Builder.FENDER, 'new', Type.AUCOUSTIC, Wood.MAHAGONY, Wood.MAHAGONY,12)
specification_2 = GuitarSpecs(Builder.MARTIN, 'old', Type.ELECTRIC, Wood.INDIAN_ROSEWOOD, Wood.MAHAGONY)
specification_3 = GuitarSpecs(Builder.FENDER, 'new', Type.AUCOUSTIC, Wood.INDIAN_ROSEWOOD, Wood.INDIAN_ROSEWOOD)
specification_4 = MandolinSpecs(Builder.FENDER, 'new', Type.OCTAVE, Wood.INDIAN_ROSEWOOD, Wood.INDIAN_ROSEWOOD,Style.A_STYLE)

guitar_1 = Guitar('2134', 34.5, specification_1)
guitar_2 = Guitar('1234', 44.5, specification_2)
guitar_3 = Guitar('2222', 69.5, specification_3)
mandolin_1 = Mandolin('1098', 79.3, specification_4)

print(guitar_2.__dict__)
print(mandolin_1.__dict__)

inventory_1 = Inventory()
inventory_1.add_instrument(guitar_1)
inventory_1.add_instrument(guitar_2)
inventory_1.add_instrument(guitar_3)
inventory_1.add_instrument(mandolin_1)

g = inventory_1.search_instrument(specification_4)
print("search mandolin")
for elem in g:
    print(elem.to_dict())
