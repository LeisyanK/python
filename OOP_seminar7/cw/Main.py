# Пишем приложение на python с учетом концепций ООП(Наследование, полиморфизм, инкапсуляция)
# Необходимо: Создать два класс наследника dog и cat с общим родителем animal. А так же класс для работы с ними vet_service. Необходимо придерживаться концепций ООП, а так же желательно код-стайла языка python(snake_case)

from Vet_service import *


cat1 = Cat("Barsik", 5, 25, False)
dog1 = Dog("Sharik", 7, 28, True)
#list_animal = Vet_service.add_animal(cat1)
list_animal = Vet_service()
#list_animal = []
#Vet_service(list_animal)
list_animal.add_animal(cat1)
list_animal.add_animal(dog1)
print("list_animal: ", list_animal)
list_animal.print_list()
print("------------------------")
print("Удалила кошку")
list_animal.del_animal(cat1)
list_animal.print_list()
