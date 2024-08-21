from dataclasses import dataclass

@dataclass
class Car:
    _brand: str
    _price: float

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value