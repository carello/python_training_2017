class Scoop(object):
    def __init__(self, flavor):
        self.flavor = flavor

s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('coffee')
s4 = Scoop('kiwi')
s5 = Scoop('mellon')
s6 = Scoop('avacdo')

#print s1.flavor
#for one_scoop in [s1, s2, s3]:
#    print one_scoop.flavor

# is-a relaltionship : inheritance
# has-a relationship : composition

print "%" * 80

class Cone(object):
    max_scoops = 3
    def __init__(self):
        self.scoops = []


    def add_scoops(self, *args):
        #if len(self.scoops) < self.max_scoops:
        #    self.scoops += args
        self.scoops += args[:Cone.max_scoops - len(self.scoops)]

    def flavor(self):
        return [one_scoop.flavor
                for one_scoop in self.scoops]


c = Cone()
c.add_scoops(s1, s2)
c.add_scoops(s3)
c.add_scoops(s4)
print c.flavor()



print "A"
class Person(object):
    print "B"
    def __init__(self, name):
        print "C"
        self.name = name

    print "D"
print "E"

p1 = Person('name1')
p2 = Person('name2')
print vars(Person)

print "&" * 80

class Thermostat(object):
    def __init__(self):
        self.temp = 25


    def set_temp(self, temp):
        hi_temp = 50
        lo_temp = 10
        if temp > hi_temp:
            raise ValueError("too high!")
        if temp < lo_temp:
            raise ValueError("too low")
        else:
            self.temp = temp

    def get_temp(self):
        return self.temp

t = Thermostat()
t.set_temp(25)
t.set_temp(15)
print t.get_temp()


print "&" * 80

class Cone(object):
    max_scoops = 3
    def __init__(self):
        self.scoops = []


    def add_scoops(self, *args):
        #if len(self.scoops) < self.max_scoops:
        #    self.scoops += args
        self.scoops += args[:self.max_scoops - len(self.scoops)]

    def flavor(self):
        return [one_scoop.flavor
                for one_scoop in self.scoops]

class BigCone(Cone):
    Cone.max_scoops = 5





c = Cone()
c.add_scoops(s1, s2)
c.add_scoops(s3)
c.add_scoops(s4)
print c.flavor()

bc = BigCone()
bc.add_scoops(s1, s2)
bc.add_scoops(s3, s4, s5, s6)
print bc.flavor()
