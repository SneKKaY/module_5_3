class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors:
            print("The floor doesn't exist")
        else:
            for i in range(new_floor):
                print(i+1)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название {self.name}, количество этажей {self.number_of_floors} '

h1 = House('ЖК Горский', 18)
h1.go_to(5)

h2 = House('Домик в деревне', 2)
h2.go_to(10)


# __str__

print(h1)

print(h2)



# __len__

print(len(h1))

print(len(h2))

