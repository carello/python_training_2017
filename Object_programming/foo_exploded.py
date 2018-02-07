
class Foo(object):
    def __init__(self, x):
        self.x = x

    def x2(self):
        return self.x * 2

f = Foo(10)
print f.x2()
# exploded internally is:
print Foo.x2(f)

print id(Foo.x2)



