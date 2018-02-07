

class Scoop(object):
    def __init__(self, flavor):
        self.flavor = flavor

class Cone(object):
    max_scoops = 3

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *args):
        for one_scoop in args:
            if len(self.scoops) >= Cone.max_scoops:     # could use self.max_scoops instead of Cone.max_scoops
                break
            self.scoops.append(one_scoop)
        # Alternative way to do this, cool but hard to read
        # self.scoops += args[:Cone.max_scoops - len(self.scoops)]


    def flavors(self):
        return [one_scoop.flavor
                for one_scoop in self.scoops]


s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('coffee')
s4 = Scoop('kiwi')


#for one_scoop in [s1, s2, s3]:
#    print one_scoop.flavor

c = Cone()  # should hold a max of 3 scoops
c.add_scoops(s1, s2)
c.add_scoops(s3)
c.add_scoops(s4)
print c.flavors()


