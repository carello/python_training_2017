# population = 0    # global, okay works but not best
# using a variable on class is a nice way to do this, Person.population, if the variable
# will be changing. Global is okay if it will stay a fixed value.

class Person(object):
    def __init__(self, name):
        self.name = name

        #global population  # old global method
        #population += 1    # old global method
        Person.population += 1

    def greet(self):
        return "hello, {0}".format(self.name)

Person.population = 0
p1 = Person('chet')
p2 = Person('connie')
p3 = Person('ray')
print "Population: {0}".format(Person.population)
print p1.greet()
#print Person.greet(p1)  # same as previous line

# #############################
# BETTER WAY
print "*" * 100

class Person(object):
    population = 0  # adding attribute to class
    def __init__(self, name):
        self.name = name
        Person.population += 1

    def greet(self):
        return "hello, {0}".format(self.name)


print "Population BC: {0}".format(Person.population)
p1 = Person('chet')
p2 = Person('connie')
p3 = Person('ray')
print "Population AD: {0}".format(Person.population)
print p1.greet()

#print vars(Person)
# so population is jointly owned, per below...
# Shared path starts on instance, then class, then class parent, then object.
# search is heirarchical and 1st one wins, this is how intheritance works.
# put on class, if it doesn't change, put on instance if it will change.

print "P1.population: {}".format(p1.population)
print "P2.population: {}".format(p2.population)
print "P3.population: {}".format(p3.population)
