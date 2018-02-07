


def add_scoops(*args):
    scoops = []
    scoops += args
    print scoops

def add_scoops2(*args):
    scoops2 = []
    scoops2.append(args)
    print scoops2
#
# my_list = []
#
# my_list.append("s")
# my_list.append("a")
# my_list.append("w")
#
# print my_list
#
# my_list2 = []
#
# my_list2 += 't'
# my_list2 += 'a'
# my_list2 += 'y'
#
# print my_list2

add_scoops('s1: 4', 's2: 5', 's3: 6')
add_scoops2('s1: 4', 's2: 5', 's3: 6')

class Foo(object):
    def __init__(self, x):
        self.x = x

f = Foo(10)
print f
print len(f)
