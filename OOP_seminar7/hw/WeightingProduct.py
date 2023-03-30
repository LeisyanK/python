from Product import *


class WeightingProduct(Product):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self._weight = weight

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, new_weight):
        self._weight = new_weight

    def __str__(self):
        # return self.name + " " + str(self.price) + " " + str(self._weight)
        return f'{self.name} {self.price} {self._weight}'