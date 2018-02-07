# Create a Timing decorator
# When we invoke a function that has the Timing decorator,
# write to a file ('x.txt): the name of the function, the start time, the end time, and total run time.
# useful stuff:
#   time.time and time.sleep(x)
# don't do stdout manipulation

import time

class Timer(object):
    def __init__(self, f):
        self.f = f
        self.filename = 'mytime_1.txt'

    def __call__(self, *args, **kwargs):

        with open(self.filename, 'a') as f:
            start_time = time.time()
            value = self.f(*args, **kwargs)
            end_time = time.time()
            f.write("{}\t{}\t{}\n".format(self.f.__name__,
                                            start_time,
                                            end_time - start_time))
        return value


@Timer
def add(x, y):
    time.sleep(3)
    return x * y

print add(20, 30)


############
# METHOD 2 using FUNCTIONS
# do the same previous example using functions instead
# import time
#
# def memo(f):    # this is like __init__. outer function runs at creation time
#     cache = {}
#
#     def inner(*args):    # this is __call__. inner runs at run time
#         if args not in cache:
#             cache[args] = f(*args)
#         return cache[args]
#     return inner
#
# @memo
# def add(x, y):
#     time.sleep(3)
#     return x + y
# #add = memo(add)
#
# print add(10, 20)
# print add(10, 20)
print " * " * 60
def Memo(f):
    cache = {}

    def inner(*args, **kwargs):
        if args not in cache:
            cache[args] = f(*args, **kwargs)
        return cache[args]
    return inner

@Memo
def add(a, b):
    return a + b

print add(10, 20)

#######
