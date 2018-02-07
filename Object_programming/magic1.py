class Foo(object):
    def __init__(self, x):
        self.x = x

    def __repr__(self):
        return "[repr] Instance of Foo vars = {}".format(vars(self))

    def __len__(self):
        return 333

f = Foo(10)

print f
print len(f)


