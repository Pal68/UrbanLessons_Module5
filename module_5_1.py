class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor not in range(1, self.number_of_floors+1):
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor+1):
                print(i)

house1 = House('ЖК Мелодия', 27)
house2 = House("Хрущевки", 5)
house1.go_to(5)
house2.go_to(27)


