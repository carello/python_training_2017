# TASK 1
# create Scoop class
# s1 = Scoop('vanilla')
# s2 = Scoop('mellon')
# s3 = Scoop('kiwi')
# print s1.flavor
# for one_scoop in [s1, s2, s3]
#   print one_scoop.flavor
#############################
# TASK 2
# create Cone class
# create method to add scoops s1, s2 etc..
# print c.flavors() by calling a method, returning a list of strings
# try also print c.scoops (they will look the same)
#############################
# TASK 3
# make max scoops into a cone = 3 and print
#############################
# TASK 4
# make new class BigCone that can hold 5 scoops and print
#############################
class Cone(object):
    def __init__(self, flavor):
        self.flavor = flavor

s1 = Cone('kiwi')
s2 = Cone('berry')
s3 = Cone('mellon')
s4 = Cone('feet')
s5 = Cone('vanilla')
s6 = Cone('cocoa')

# for one_cone in [s1,s2,s3,s4,s5,s6]:
#     print one_cone.flavor
# print s1.flavor

class Cone(object):
    max_scoops = 3
    def __init__(self):
        self.scoops = []

    def add_scoops(self, *args):
        for one_scoop in args:
            if len(self.scoops) < self.max_scoops:
                self.scoops.append(one_scoop)

    def flavors(self):
        return [one_scoop.flavor
                for one_scoop in self.scoops]


class BigCone(Cone):
    max_scoops = 5


c1 = Cone()
c1.add_scoops(s1, s2, s3, s4, s5)
c2 = Cone()
c2.add_scoops(s6, s6)
print c1.flavors()
print c2.flavors()
bc = BigCone()
bc.add_scoops(s6,s5,s5,s3,s1,s2)
print bc.flavors()

