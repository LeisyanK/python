from VendingMachine import *


class VendingMachineBottle(VendingMachine):
    def __init__(self, name):
        super().__init__(name)

    def init_product(self, prod):
        # super()._product_list = prod
        super()._product_list.append(prod)