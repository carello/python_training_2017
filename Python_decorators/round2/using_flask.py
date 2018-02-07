###############
# time 3:00
# this following example is often used in Flask, though its hidden mostly
def max_n_times(n):
    def deco(f):
        remaining = list(range(n))

        def inner(*args):
            if not remaining:
                raise ValueError("too many times")

            remaining.pop()

            return f(*args)

        return inner
    return deco

@max_n_times(3)
def add(a, b):
    """This is my help: will add 2 things together"""
    return a + b
# this will be a function in a function in a function
#add = max_n_times(7)(add)

#print help(add)

for i in range(10):
    print add(i, i)
