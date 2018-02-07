# TASK 1
# Create Animal class with attributes: color, species, num_legs
# Animal class should be able to provide a print out of Animals
# Create Classes of: Wolf, Sheep, Snake, Parrot. Attribute 'color'
# Try to optimize classes. Hint - try inheritance.
# #############################################################
# TASK 2
# Create Cage class: attribute cage_id
# You should be able to add animals to the cage
# should be able to print: Cage: animals...
# #############################################################
# TASK 3
# Create class Zoo.
# Add cages to the zoo and be able to print out Zoo: Cage: animals...
# Be able to print out by animal color.
# be able to get total number of legs for all animals combined.
# #############################################################


class Animals(object):
    def __init__(self, color, num_legs):
        self.species = type(self).__name__
        self.color = color
        self.num_legs = num_legs
    def __repr__(self):
        return "{}, {}, legs: {}".format(self.species, self.color, self.num_legs)

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
    def add_animals(self, *args):
        self.animals += args
    def __repr__(self):
        output = "\nCage: {}".format(self.cage_id)
        output += '\n'.join(['\t' + str(one_animal)
                             for one_animal in self.animals])
        return output

class Zoo(object):
    def __init__(self):
        self.cages = []
    def add_cages(self, *args):
        self.cages += args
    def __repr__(self):
        return "Zoo:" + '\n'.join([str(one_cage)
                                  for one_cage in self.cages])
    def get_animal_color(self, color):
        return '\n'.join([str(one_animal)
                          for one_cage in self.cages
                          for one_animal in one_cage.animals
                          if one_animal.color == color])
    def omni_legs(self):
        tot_legs = sum([legs.num_legs
                        for one_cage in self.cages
                        for legs in one_cage.animals])
        return "Total legs: {}".format(str(tot_legs))


wolf = Wolf('black')
sheep1 = Sheep('white')
sheep2 = Sheep('white')
snake = Snake('brown')
parrot = Parrot('red')

c1 = Cage(1)
c2 = Cage(2)
c1.add_animals(wolf, sheep1, sheep2)
c2.add_animals(snake, parrot)

z = Zoo()
z.add_cages(c1, c2)
print z
print "%" * 100
print z.get_animal_color('white')
print "%" * 100
print z.omni_legs()
print "%" * 100
# print c1
# print c2

# print '\n'+'%' * 60
# print wolf
# print sheep1
# print sheep2
# print snake
# print parrot



