class Animal(object):
    def __init__(self, species, color, num_legs):
        self.species = species
        self.color = color
        self.num_legs = num_legs


class Cage(Animal):
    def __init__(self, species, color, num_legs, cage_id):
        Animal.__init__(self, species, color, num_legs)
        self.cage_id = cage_id

    def add_animals(self, *args):
        pass




c1 = Cage(1)
c2 = Cage(2)

wolf = Animal('wolf', 'black', 4)
sheep1 = Animal('sheep1', 'white', 4)
sheep2 = Animal('sheep2', 'white', 4)
snake = Animal('snake', 'brown', 0)
parrot = Animal('parrot', 'black', 2)

print wolf
print sheep1
print sheep2
print snake
print parrot

