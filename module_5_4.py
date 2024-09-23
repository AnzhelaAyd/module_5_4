class Hous:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        name=args[0]
        cls.houses_history.append(name)
        return object.__new__(cls)


    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return self.name


    def go_to(self,new_floors):
        if (new_floors < 0) or (new_floors > self.number_of_floors) :
            print('такого этожа не существует ')
        else:
            for i in range(1, new_floors+1):
                  print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
         return f'Название:  {self.name}, кол-во этажей: , {self.number_of_floors}'

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors


    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
            return self

    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
            return self

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
            return self

    def __del__(self):
        print(self.name, 'снесён, но он останется в истории')




h1 = Hous('ЖК Эльбрус', 10)
print(Hous.houses_history)
h2 = Hous('ЖК Акация', 20)
print(Hous.houses_history)
h3 = Hous('ЖК Матрёшки', 20)
print(Hous.houses_history)

# Удаление объектов
del h2
del h3

print(Hous.houses_history)
