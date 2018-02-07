import sys
import time

print "*" * 200
print "*" * 200

'''
class MyTime(object):
    def __init__(self, f):
        self.f = f
        self.filename = 'mytime.txt'

    def __call__(self, *args, **kwargs):
       
    
        with open(self.filename, 'w') as f:
            start_time = time.time()
            value = self.f(*args, **kwargs)
            end_time = time.time()
            
            f.write(start_time, end_time)
        
            return value

@MyTime
def get_time():
    print "TIME..."

get_time()


class Memorize(object):
    def __init__(self, f):
        self.f = f
        self.cache = {}

    def __call__(self, *args, **kwargs):
        if args not in self.cache:
            print "FIST TIME"
            self.cache[args] = self.f(*args)
        else:
            print "in cache, not exec"
        return self.cache[args]



@Memorize
def add(a, b):
    time.sleep(3)
    return a + b
# its doing this: add = Memoris(add)

print add(2,2)
print add(2,2)


def memo(f):    # __init__ - out function at createtion time
    cache = {}

    def inner(*args):       # __call__ being run at run-time
        if args not in cache:
            cache[args] = f(*args)

        return cache[args]
    return inner

@memo
def add(a, b):
    time.sleep(3)
    return a + b
# add = memo(add)

print add(2,2)
print add(2,2)


print "9" * 100
'''
# #############################
import time
import sys

def add_timestamp(c):
    def inner(*args):
        new_instance = c(*args)
        new_instance.timstamp = time.time()
        return new_instance
    return inner

@add_timestamp
class Foo(object):
    def __init__(self, x):
        self.x = x

    def x2(self):
        return self.x * 2


f = Foo(10)
vars(f)

print f
print vars(f)

