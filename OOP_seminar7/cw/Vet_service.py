from Cat import Cat
from Dog import Dog
from Animal import *


class Vet_service:
    def __init__(self):
        list1 = []
        self._list = list1

    def add_animal(self, animal):
        self._list.append(animal)

    def del_animal(self, animal):
        self._list.remove(animal)

    def print_list(self):
        print(self._list)
        for i in range(len(self._list)):
            print(self._list[i]) #.to_string())  # здесь срабатывает def __str__(self) без вызова

        # методы to_string() и def __str__(self) работают одинаково. Последний стандартный (первый - мой самописный)
        for el in self._list:
            print(el.to_string())