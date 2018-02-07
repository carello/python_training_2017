class Person(object):
    population = 0  # adding attribute to class

    def __init__(self, name):
        self.name = name
        Person.population += 1  # this will search for population in the Person object

        # DONT DO THESE. You're are creating a new population variable on the instance!
        # RULE never set self on a instance, use parent. Okay to use self if retrieving information
        #self.population += self.population = 1
        #self.population += 1

    def greet(self):
        return "hello, {0}".format(self.name)


print "Population BC: {0}".format(Person.population)
p1 = Person('chet')
p2 = Person('connie')
p3 = Person('ray')
print "Population AD: {0}".format(Person.population)
print p1.greet()
