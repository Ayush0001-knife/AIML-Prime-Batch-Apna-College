class Herbivore:
    def eat_plants(self):
        print("I eat plants.")

class Carnivore:
    def eat_meat(self):
        print("I eat meat.")

class Omnivore:
    def eat_both(self):
        print("I eat both plants and meat.")

class Bear(Herbivore, Carnivore, Omnivore):
    def __init__(self, name):
        self.name = name


b = Bear("Brown Bear")

b.eat_plants()
b.eat_meat()
b.eat_both()