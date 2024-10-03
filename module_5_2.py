class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        
    def go_to(self, new_floor):
        new = range(new_floor)
        if self.number_of_floors < new_floor:
            print("Ошибка")
        else:
            for i in new:
                print(i)
                if (i + 1) == new_floor:
                    print(new_floor)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f"Название:{self.name} , кол-во этажей: {self.number_of_floors}")

jotoro = House("ЖК Кифир", 26)
jojo = House("ЖК Дыра", 10)
#__len__
print(len(jotoro))
print(len(jojo))

#__str__
print(jojo)
print(jotoro)
#def __str__(self):
#    return print(f"Название:{self.name} , кол-во этажей: {self.number_of_floors}")

