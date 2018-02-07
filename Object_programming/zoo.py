
class Animal(object):
    def __init__(self, color, number_of_legs):
        self.color = color
        #self.species = species
        # alternative is we can use __name__ space
        self.species = type(self).__name__.upper()
        self.number_of_legs = number_of_legs

    def __repr__(self):
        return "{} {}, {} legs".format(self.color,
                                       self.species,
                                       self.number_of_legs)

class Wolf(Animal):
    def __init__(self, color):
        Animal.__init__(self, color, 4)

class Sheep(Animal):
    def __init__(self, color):
        Animal.__init__(self, color, 4)

class Snake(Animal):
    def __init__(self, color):
        Animal.__init__(self, color, 0)

class Parrot(Animal):
    def __init__(self, color):
        Animal.__init__(self, color, 2)

wolf = Wolf('black')
sheep1 = Sheep('white')
sheep2 = Sheep('white')
snake = Snake('brown')
parrot = Parrot('red')

print wolf
print sheep1
print sheep2
print snake
print parrot

class Cage(object):
    def __init__(self, id_number):
        self.id_number = id_number
        self.animals = []

    def add_animals(self, *args):
        self.animals += args

    def __repr__(self):
        output = 'Cage {}\n'.format(self.id_number)
        output += '\n'.join(['\t' + str(one_animal)
                             for one_animal in self.animals])
        #for one_animal in self.animals:
        #    output += '\t' + str(one_animal) + '\n'
        return output

c1 = Cage(1)
c1.add_animals(wolf, sheep1, sheep2)
print "*" * 100
print c1

c2 = Cage(2)
c2.add_animals(snake, parrot)
print c2
# this is doing samething a __repr__ , but with repr it's part of the class - cleaner I guess...
#for one in c1.animals:
#    print str(one)

class Zoo(object):
    def __init__(self):
        self.cages = []

    def add_cages(self, *args):
        self.cages += args

    def __repr__(self):
        print "%%%%%%%%%%%%%%%%%%"
        return 'Zoo:\n' + '\n'.join([str(one_cage)
                            for one_cage in self.cages])

    def animals_by_color(self, color):
        return '\n'.join([str(one_animal)
                          for one_cage in self.cages
                          for one_animal in one_cage.animals
                          if one_animal.color == color])

    def number_of_legs(self):
        return sum([one_animal.number_of_legs
                    for one_cage in self.cages
                    for one_animal in one_cage.animals])


#print "Zoo:"
z = Zoo()
z.add_cages(c1, c2)
print z
print z.animals_by_color('red')
print z.number_of_legs()