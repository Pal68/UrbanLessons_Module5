class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название:  {self.name}, количество этажей: {self.number_of_floors}"

    def __eq__(self, other):
        try:
            return self.number_of_floors == other.number_of_floors
        except Exception:
            print(f"Не могу конвертировать {type(other)} в тип {type(self)}")

    def __lt__(self, other):
        try:
            return self.number_of_floors < other.number_of_floors
        except Exception:
            print(f"Не могу конвертировать {type(other)} в тип {type(self)}")

    def __gt__(self, other):
        try:
            return self.number_of_floors > other.number_of_floors
        except Exception:
            print(f"Не могу конвертировать {type(other)} в тип {type(self)}")

    def __le__(self, other):
        try:
            return self.number_of_floors <= other.number_of_floors
        except Exception:
            print(f"Не могу конвертировать {type(other)} в тип {type(self)}")

    def __qe__(self, other):
        try:
            return self.number_of_floors >= other.number_of_floors
        except Exception:
            print(f"Не могу конвертировать {type(other)} в тип {type(self)}")

    def __ne__(self, other):
        try:
            return self.number_of_floors != other.number_of_floors
        except Exception:
            print(f"Не могу конвертировать {type(other)} в тип {type(self)}")

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
house2 = House("ЖК Акация", 20)

print(house1)
print(house2)
print(house1 == house2) # __eq__

house1 = house1 + 10 # __add__
print(house1)
print(house1 == house2)

house1 += 10 # __iadd__
print(house1)

house2 = 10 + house2 # __radd__
print(house2)

print(house1 > house2) # __gt__
print(house1 >= house2) # __ge__
print(house1 < house2) # __lt__
print(house1 <= house2) # __le__
print(house1 != house2) # __ne__


