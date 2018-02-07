class Animals(object):
    def __init__(self, color, num_legs):
        self.color = color
        self.species = type(self).__name__
        self.num_legs = num_legs

    def __repr__(self):
        return "{0} is {1} with {2} legs".format(self.species, self.color, self.num_legs)

class Wolf(Animals):
    def __init__(self, color):
        Animals.__init__(self, color, 4)

class Sheep(Animals):
    def __init__(self, color):
        Animals.__init__(self, color, 4)

class Snake(Animals):
    def __init__(self, color):
        Animals.__init__(self, color, 0)

class Parrot(Animals):
    def __init__(self, color):
        Animals.__init__(self, color, 2)


class Cage(object):
    def __init__(self, cage_id):
        self.cage_id = cage_id
        self.animals = []

    def add_animal(self, *args):
        self.animals += args

    def __repr__(self):
        output = "\nCage {}:".format(self.cage_id)
        output += "\n".join(['\t' + str(one_animal)
                             for one_animal in self.animals])
        return output

class Zoo(object):
    def __init__(self):
        self.cages = []

    def add_cages(self, *args):
        self.cages += args

    def __repr__(self):
        return '*'*60 + '\nZoo:\n' + '\n'.join([str(one_cage)
                                                for one_cage in self.cages])

    def animals_by_color(self, color):
        return '\n' + '\n'.join([str(one_animal)
                          for one_cage in self.cages
                          for one_animal in one_cage.animals
                          if one_animal.color == color])

    def get_legs(self):
        sum_legs = sum([one_animal.num_legs
             for one_cage in self.cages
             for one_animal in one_cage.animals])
        return '\n' + 'Legs = ' + str(sum_legs)


wolf = Wolf('black')
sheep1 = Sheep('white')
sheep2 = Sheep('white')
snake = Snake('brown')
parrot = Parrot('red')
# print wolf
# print sheep1
# print sheep2
# print snake
# print parrot

c1 = Cage(1)
c1.add_animal(wolf, sheep1, sheep2)
c2 = Cage(2)
c2.add_animal(snake, parrot)
print c1
print c2

z = Zoo()
z.add_cages(c1, c2)
print z
print z.animals_by_color('red')
print z.get_legs()
