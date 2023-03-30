from Product import Product


class BottleOfWater(Product):
    def __init__(self, name, price, volume):
        super().__init__(name, price)
        self._volume = volume

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, new_volume):
        self._volume = new_volume

    def __str__(self):
        # return self.name + " " + str(self.price) + " " + str(self._volume)
        return f'{self.name} {self.price} {self._volume}'

