class House:
    houses_history = []

    def __new__(cls, *args):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f"{self.name} снесён, но останется в истории")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название:  {self.name}, количество этажей: {self.number_of_floors}"

    def __eq__(self, other):
        try:
            return self.number_of_floors == other.number_of_floors
        except Exception as e:
            print(f"Ошибка {e.__str__()}")

    def __lt__(self, other):
        try:
            return self.number_of_floors < other.number_of_floors
        except Exception as e:
            print(f"Ошибка {e.__str__()}")

    def __gt__(self, other):
        try:
            return self.number_of_floors > other.number_of_floors
        except Exception as e:
            print(f"Ошибка {e.__str__()}")

    def __le__(self, other):
        try:
            return self.number_of_floors <= other.number_of_floors
        except Exception as e:
            print(f"Ошибка {e.__str__()}")

    def __qe__(self, other):
        try:
            return self.number_of_floors >= other.number_of_floors
        except Exception as e:
            print(f"Ошибка {e.__str__()}")

    def __ne__(self, other):
        try:
            return self.number_of_floors != other.number_of_floors
        except Exception as e:
            print(f"Ошибка {e.__str__()}")

    def __add__(self, other):
        try:
            self.number_of_floors=self.number_of_floors + other
            return self
        except Exception as e:
            print(f"Ошибка {e.__str__()}")

    def __iadd__(self, other):
        try:
            return self.__add__(other)
        except Exception as e:
            print(f"Ошибка {e.__str__()}")

    def __radd__(self, other):
        try:
            return self.__add__(other)
        except Exception as e:
            print(f"Ошибка {e.__str__()}")

    def go_to(self, new_floor):
        if new_floor not in range(1, self.number_of_floors+1):
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor+1):
                print(i)

house1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
house2 = House('ЖК Акация', 20)
print(House.houses_history)
house3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del house2
del house3
print(House.houses_history)
