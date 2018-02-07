# prefix notation (Polish notation)
'''
get_data = raw_input("enter calcuation: ")

s_data = get_data.split()

if s_data[0] == "+":
    cal = int(s_data[1]) + int(s_data[2])
    print cal
elif s_data[0] == "-":
    cal = int(s_data[1]) - int(s_data[2])
    print cal
elif s_data[0] == "*":
    cal = int(s_data[1]) * int(s_data[2])
    print cal
elif s_data[0] == "/":
    cal = int(s_data[1]) / int(s_data[2])
    print cal
'''

def lines(f):
    def inner():
        print '-' * 60
        f()
        print '-' * 60
    return inner

def a():
    print 'a!'
a = lines(a)

def b():
    print 'b!'
b = lines(b)

a()
b()

import sys


def alt_stdout(f, temp_stdout):
    def inner():
        old_stdout = sys.stdout
        sys.stdout = temp_stdout
        f()
        sys.stdout = old_stdout
    return inner

my_temp_stdout = open('mystdout.txt', 'w')

def a():
    print "A!"
a = alt_stdout(a, my_temp_stdout)

def b():
    print "B!"
b = alt_stdout(b, my_temp_stdout)

a()
b()
my_temp_stdout.close()



print "*" * 100

def lines(f):
    def inner():
        print '$',
        f()
        print '-' * 60
    return inner

@lines
def a():
    print 'a!'
# its doing this: a = lines(a)

@lines
def b():
    print 'b!'
# its doing this: b = lines(b)

a()
b()

print "*" * 100
print "*" * 100
print "*" * 100

class Lines(object):
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        print "$",
        self.f(*args)
        print "_" * 60

@Lines
def a():
    print 'AA!'
# its doing this: a = Lines(a)

@Lines
def b():
    print 'BB!'
# its doing this: b = Lines(b)

a()
b()


print "*" * 100
print "*" * 100

import sys
class StdOutToFile(object):
    def __init__(self, f):
        self.f = f
        self.stdout = 'mySSS.txt'

    def __call__(self, *args, **kwargs):
        old_stdout = sys.stdout
        with open(self.stdout, 'a') as sys.stdout:
            print "$",
            self.f(*args)
            print "_" * 60
        sys.stdout = old_stdout


@StdOutToFile
def mul(x, y):
    print x * y

mul(10, 500)


print "*" * 200
print "*" * 200

import sys
class StdOutToFile(object):
    def __init__(self, f):
        self.f = f
        self.stdout = 'mySSS.txt'

    def __call__(self, *args, **kwargs):
        old_stdout = sys.stdout

        with open(self.stdout, 'a') as sys.stdout:
            result = self.f(*args, **kwargs)

        sys.stdout = old_stdout
        return result

@StdOutToFile
def mul(x, y):
    return x * y

print mul(10, 500)
