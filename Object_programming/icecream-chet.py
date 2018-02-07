

class Scoop(object):
    def __init__(self, flavor):
        self.flavor = flavor

class Cone(object):
    def __init__(self):
        self.scoops = []

    def add_scoops(self, *args):
        self.scoops += args

    def flavors(self):
        return [one_scoop.flavor
                for one_scoop in self.scoops]


s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('coffee')


#for one_scoop in [s1, s2, s3]:
#    print one_scoop.flavor

c = Cone()
c.add_scoops(s1, s2)
c.add_scoops(s3)
print c.flavors()



