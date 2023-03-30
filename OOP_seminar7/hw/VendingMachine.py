# from Product import Product
# from BottleOfWater import *
# from WeightingProduct import *


class VendingMachine:
    def __init__(self):
        # self._name_mach = name
        self._product_list = []

    # @property
    # def name_mach(self):
    #     return self._name_mach
    #
    # @name_mach.setter
    # def name_mach(self, new_name):
    #     self._name_mach = new_name

    # @property
    # def product_list(self):
    #     return self._product_list

    # @product_list.setter
    # def product_list(self, new_list):
    #     self._product_list = new_list

    def init_product(self, prod):
        self._product_list.append(prod)

    def get_product(self, search):
        for i in range(len(self._product_list)):
            if self._product_list[i].name == search:
                print(self._product_list[i])

    def print_products(self):
        # print(self._product_list)
        for el in self._product_list:
            print(el)