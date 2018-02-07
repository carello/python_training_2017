class Scoops(object):
    def __init__(self, flavor):
        self.flavor = flavor

s1 = Scoops('vanilla')
s2 = Scoops('strawberry')
s3 = Scoops('chocolate')
s4 = Scoops('sausage')
s5 = Scoops('mellon')
s6 = Scoops('feet')

# flavor_list = ([one_scoop.flavor
#         for one_scoop in [s1,s2,s3,s4,s5,s6]])
#
# for one_scoop in [s1,s2,s3,s4,s5,s6]:
#     print one_scoop.flavor

class Cone(object):
    max_scoops = 3

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *args):
        #for a in args:
        #    self.scoops.append(a)
        # self.scoops.extend(args)    # Could use += instead of extend. Extend is like an iterable
        # following method creates the iterable manually.
        for one_scoop in args:
            if len(self.scoops) >= self.max_scoops:
                break

            self.scoops.append(one_scoop)


    def flavors(self):
        return [one_scoop.flavor
                for one_scoop in self.scoops]

class BigCone(Cone):
    max_scoops = 5




c = Cone()
c.add_scoops(s1, s2, s3)
c.add_scoops(s5, s6)
print c.flavors()

bc = BigCone()
bc.add_scoops(s6, s5, s4, s4, s2)
print bc.flavors()



