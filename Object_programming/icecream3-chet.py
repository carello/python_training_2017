
class Scoop(object):
    def __init__(self, flavor):
        self.flavor = flavor

class Cone(object):
    max_scoops = 3

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *args):
        for one_scoop in args:
            # retrieve attributes using self.max_scoops is ok - BUT don't set using self - use Cone.max_scoops
            if len(self.scoops) >= self.max_scoops:
                break
            self.scoops.append(one_scoop)

    def flavors(self):
        return [one_scoop.flavor
                for one_scoop in self.scoops]


class BigCone(Cone):
    # DONT DO THIS
    # Cone.max_scoops = 5   # dont do this.
    # ###########
    max_scoops = 5


s1 = Scoop('chocolate')
s2 = Scoop('vanilla')
s3 = Scoop('coffee')
s4 = Scoop('kiwi')
s5 = Scoop('cherry')
s6 = Scoop('mellon')

c = Cone()  # should hold a max of 3 scoops
c.add_scoops(s1, s2)
c.add_scoops(s3)
c.add_scoops(s4)
print c.flavors()

bc = BigCone()
bc.add_scoops(s1, s2)
bc.add_scoops(s3, s4, s5)
print bc.flavors()

