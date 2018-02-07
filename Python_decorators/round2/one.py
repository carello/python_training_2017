############################
#   POLISH NOTATION
#   PREFIX NOTATION
############################
# + 2 3 (operator int int)
######################
# METHOD ONE (classic)
# def add(x, y):
#     return int(x) + int(y)
# def sub(x, y):
#     return int(x) - int(y)
# def mul(x, y):
#     return int(x) * int(y)
# def divi(x, y):
#     return int(x) / int(y)
#
# op, first, second = raw_input("Enter notation: ").split()
#
# if op == '+':
#     print add(first, second)
# elif op == '-':
#     print sub(first, second)
# elif op == '*':
#     print mul(first, second)
# elif op == '/':
#     print divi(first, second)
# else:
#     print "unknown"

########################
# METHOD TWO (better)
# instead create a dictionary
#op, first, second = raw_input("Enter notation: ").split()

# could set INT here instead on functions.
# first = int(first)
# second = int(second)

# def add(x, y):
#     return int(x) + int(y)
# def sub(x, y):
#     return int(x) - int(y)
# def mul(x, y):
#     return int(x) * int(y)
# def divi(x, y):
#     return int(x) / int(y)
#
# ops = {'+': add,
#        '-': sub,
#        '*': mul,
#        '/': divi}
#
# print ops[op](first, second)

#####################
# METHOD THREE (best)
# import operator
#
# ops = {'+': operator.add,
#        '-': operator.sub,
#        '*': operator.mul,
#        '/': operator.div}
#
#
# # instead create a dictionary
# to_solve = raw_input("Enter notation: ")
# op, first, second = to_solve.split()
#
#
# first = int(first)
# second = int(second)
#
# print ops[op](first, second)
#
# # cool trick example
# numbers = [100, 6]
# #print ops['+'](numbers)   # this will fail because numbers is seen as only one argument
# print ops['+'](*numbers)  # splat works, because python takes each num (argument) seperately!

############################
#   DRY
############################
# how to not repeat yourself - DRY
# this ain't soo good, works but poor code
# def a():
#     print "-" * 60
#     print 'a!'
#     print "-" * 60
#
# def b():
#     print "-" * 60
#     print 'b!'
#     print "-" * 60
#
# a()
# b()

#################
#instead do this.
# this ain't soo good, works but poor code
# def a():
#     print 'a!'
#
# def b():
#     print 'b!'
#
# def lines(f):
#     print '-' * 60
#     f()
#     print '-' * 60
#
# lines(a)    # here we are passing function a as a variable, and lines(a) executes
# lines(b)    # here we are passing function b as a variable, and lines(b) executes

#####################
# However moving more towards decorators try this:
# def a():
#     print 'a!'
#
# def b():
#     print 'b!'
#
# def lines(f):
#     def inner():
#         print '-' * 60
#         f()
#         print '-' * 60
#     return inner
#
# print lines(a)  # here we are getting back the inner function object: <function inner at 0x101832cf8>
# print lines(b)  # here we are getting back the inner function object: <function inner at 0x101832cf8>
#
# # to execute a function object, we need () to make it callable.
# lines(a)()
# lines(b)()
#
# # but do this.
# a = lines(a)
# b = lines(b)
# a() # note this isn't def a, its <function inner at 0x101832cf8>
# b() # note this isnt' def b, its <function inner at 0x101832cf8>
#

###########################
#   END GAME DECORATORS
###########################
# # so a better way to see this and closer to what decorators are doing is:
#
# def lines(f):
#     def inner():
#         print '-' * 60
#         f()
#         print '-' * 60
#     return inner
#
# def a():
#     print 'a!'
# a = lines(a)
#
# def b():
#     print 'b!'
# b = lines(b)
#
# print a     # this is object inner function <function inner at 0x102132cf8>
# print b     # this is object inner function <function inner at 0x102132c08>
#
# a()     # call it!
# b()     # call it!

###############
#   EXAMPLE
#   Time 58:20

# import sys
# # print "hello is actually the following:
# # sys.stdout.write("hello" + '\n')
# def alt_stdout(f, temp_stdout):
#     def inner():
#         old_stdout = sys.stdout
#         sys.stdout = temp_stdout
#         f()
#         sys.stdout = old_stdout
#     return inner
#
# my_temp_stdout = open('mystdout.txt', 'a')
#
# def a():
#     print "A!"
# a = alt_stdout(a, my_temp_stdout)
#
# def b():
#     print "B!"
# b = alt_stdout(b, my_temp_stdout)
#
# a()
# b()
# print "Done"
# my_temp_stdout.close()

###########
#   EXAMPLE
#   Time 1:14

# up till now we've done 'manual' decorators.
# lets convert this into a decorator
# def lines(f):   # Outer function
#     def inner():    # Inner function
#         print '-' * 60
#         f()
#         print '-' * 60
#     return inner
#
# @lines      # add this. This means: a = lines(a); execute outer function and return inner
# def a():
#     print 'a!'
# # a = lines(a)  #delete this
#
# @lines      # add this. This means: b = lines(b): execute out function and return inner
# def b():
#     print 'b!'
# # a = lines(a)  #delete this
#
# a()     # call it! Execute inner function
# b()     # call it! Execute inner function

########################
#   EXAMPLE
#   Time 1:16

############################
#   DECORATORS USING CLASSES
############################
# lets try decorators using classes to work through the logic
# class Foo(object):
#     def __init__(self, x):
#         self.x = x
#     def x2(self):
#         return self.x * 2
#     @staticmethod   # allows us to run this as a plain old function without any instance classes around it.
#     def hello():        # this is a method and we can't call it directly, need staticmethod below
#         return "Hello!"
#     #hello = staticmethod(hello) # this returns a function, which we can call (old style)
#
# f = Foo(10)
# print f.x2()
# print Foo.hello() # won't work unless we have staticmethod above

############
#   EXAMPLE CLASSMETHODS
#   Time 1:24

# Classmethods
# class Foo(object):
#     def __init__(self, x):
#         self.x = x
#     def x2(self):
#         return self.x *2
#
#     @classmethod    #must have cls as first parm. classmethod gets the class as its first arugment.
#                     # regular methods get the instance as the first arguement.
#                     # classmethod used to modify class. Static is just conviencne. Don't worry about it...
#     def hello(cls):
#         return "Hello {}".format(cls)
#         # hello = classmethod(hello)
#
# f = Foo(10)
# print Foo.hello()
# # point is python has built in decorators: static and class methods


#################
#   EXAMPLE
#   Time 1:27

# using 'get'
# import operator
# #
# ops = {'+': operator.add,
#        '-': operator.sub,
#        '*': operator.mul,
#        '/': operator.div}
#
# def generic_func(*args):
#     return "that operator doesn't exist"
#
# # instead create a dictionary
# to_solve = raw_input("Enter notation: ")
# op, first, second = to_solve.split()
#
#
# first = int(first)
# second = int(second)
#
# print ops.get(op, generic_func)(first, second)
# could use lambda in place of generic_func

##########
#   EXAMPLE
#   Time 1:30

# using classes with decorators
# class Lines(object):
#     def __init__(self, f):  # runs when decoratod function is defined
#         print "now in __init__ for {}".format(f.__name__)
#         self.f = f
#
#     def __call__(self):     # run when decorated function is called
#         print "now in __call__ for {}".format(self.f.__name__)
#         print "-" * 60
#         self.f()
#         print "-" * 60
#
# @Lines
# def a():
#     print "a!"
# # a = Lines(a)
#
# @Lines
# def b():
#     print "b!"
#
# #a.f()
# #b.f()
# a()
# b()

##############
#   EXAMPLE
#   Time 1:46:00

#
# don't forget *args!!!
# class Lines(object):
#     def __init__(self, f):  # runs when decoratod function is defined
#         print "now in __init__ for {}".format(f.__name__)
#         self.f = f
#
#     def __call__(self, *args):     # run when decorated function is called
#         print "now in __call__ for {}".format(self.f.__name__)
#         print "-" * 60
#         self.f(*args)
#         print "-" * 60
#
# @Lines
# def mul(x, y):
#     print x * y
#
# mul(10, 20)

#############
#   EXAMPLE
#   Time 1:49

# Create a decorator
# that lets you decorate any function with any number of arguements (*args)
# It will send all stdout from the function to a file
# Create a logging decorator example!:
#
# import sys
#
# class StdoutToFile(object):
#
#     def __init__(self, f):
#         #print "now in __init__ for {}".format(f.__name__)
#         self.f = f
#         self.stdout = 'mystdout.txt'
#
#     def __call__(self, *args):
#         #print "now in __call__ for {}".format(self.f.__name__)
#         old_stdout = sys.stdout
#         with open(self.stdout, 'a') as sys.stdout:
#             self.f(*args)
#         sys.stdout = old_stdout
#
#
#
# @StdoutToFile
# def mul(x, y):
#     print x * y
# # mul = StdoutToFile(mul(x, y))
#
# mul(10, 580)
# print "Done"

##############
#   EXAMPLE
#   Time 2:02

import sys

# class StdoutToFile(object):
#
#     def __init__(self, f):
#         #print "now in __init__ for {}".format(f.__name__)
#         self.f = f
#         self.stdout = 'mystdout.txt'
#
#     # this is very complete decorator - keep for reference
#     def __call__(self, *args, **kwargs):
#         #print "now in __call__ for {}".format(self.f.__name__)
#         old_stdout = sys.stdout
#         with open(self.stdout, 'a') as sys.stdout:
#             result = self.f(*args, **kwargs)
#         sys.stdout = old_stdout
#         return result
#
#
#
# @StdoutToFile
# def mul(x, y):
#     print "about to write to file"
#     print x * y
#     return x * y
# # mul = StdoutToFile(mul)
#
# mul(10, 515)
#
# print "Done"

####################################
########    GOOD EXAMPLE    ########
####################################
# Time 2:06
# Create a Timing decorator
# When we invoke a function that has the Timing decorator,
# write to a file ('x.txt): the name of the function, the start time, the end time, and total run time.
# useful stuff:
#   time.time and time.sleep(x)
# dont do stdout manipulation
#
# import time
#
# class MyTimer(object):
#
#     def __init__(self, f):
#         print "in __INIT__"
#         self.f = f
#         self.filename = 'mytime.txt'
#
#     def __call__(self, *args, **kwargs):
#
#         with open(self.filename, 'a') as f:
#             print "in__call__ A"
#             start_time = time.time()
#             value = self.f(*args, **kwargs)
#             end_time = time.time()
#             print "in__call__ B"
#             f.write('{}\t{}\t{}\n'.format(self.f.__name__,
#                                           start_time,
#                                           end_time,
#                                           end_time - start_time))
#         return value
#
# @MyTimer
# def add(a, b):
#     time.sleep(1)
#     return a + b
#
# @MyTimer
# def mul(a, b):
#     time.sleep(2)
#     return a * b
#
# print add(10, 5)
# print mul(23, 6)


############
#   EXAMPLE MEMOIZATION (CACHE)
#   time 2:22

# add(2, 2)
# add(2, 2) will produce the same result. so cache it!
# if we pass dict or list, this would die...
# import time
# class Memo(object):
#     def __init__(self, f):
#         self.f = f
#         self.cache = {}
#
#     def __call__(self, *args):
#         # If I've seen these args before, then reuse the result from them
#         # args is a tuple and we can use tuple in a dict
#         if args not in self.cache:
#             print "First time, executing function "
#             self.cache[args] = self.f(*args)
#             print self.cache
#         else:
#             print "Found in cache, not executing"
#         return self.cache[args]
#
#
#         pass
#
# @Memo
# def add(a, b):
#     time.sleep(3)
#     return a + b
#
# print add(2, 2)     # prints "First time, executing function
# print add(2, 2)      # prints "Found in cache; not executing
# print add(2, 2)      # prints "Found in cache; not executing
# print add(2, 2)      # prints "Found in cache; not executing


##############################################
#   EXAMPLE MEMOIZATION WITH FUNCTIONS INSTEAD
#   Time 2:36
##############################################

# do the same previous example using functions instead
# import time
#
# def memo(f):    # this is like __init__. outer function runs at creation time
#     cache = {}
#     print "in OUTER"
#     def inner(*args):    # this is __call__. inner runs at run time
#         print "in INNER"
#         print args
#         if args not in cache:
#             print "IN the IN"
#             print f(*args)
#             print "$$$$$$$$$"
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



###################
#   SCOPING
#   TIME 2:40
###################

# REVIEW THIS VIDEO SECTION
# Scoping. Indent doesn't change scope unless in a function
# L = local
# E = enclosing
# G = global
# B = builtins
# if in a function we start at top @ L. if not in a function we start @ G
# the closure is key: function returned from a function that has access to the outer data!
# that's how inner can remember f and cache.
# this topic is key to understanding the flows

# side note: if you running cache[arg] - the square brackets means your running a method
# Python 2: you can't change a global variable from within an inner. you can in Python3
# do decorators with functions. Classes have some restrictions.
###################

# time 2:50
#
# create function dec called 'maxfive'
# the func it decs can be called no more than 5 times
# any calls beyond 5, raises a ValueError exception

# IF PYTHON 3 We could do the following
# def maxfive(f):
#     counter = 5
#     "print OUTER: {}".format(counter)
#
#     def inner(*args):
#         nonlocal counter
#         if counter <= 0:
#             raise ValueError("too many times")
#         counter-= 1
#         return f(*args)
#     return inner
#
# @maxfive
# def add(a, b):
#     return a + b
#
# for i in range(10):
#     print(add(i, i))

# PTYHON 2 there's no nonlocal capability
# def maxfive(f):
#     remaining = list(range(5))
#     #remember list is a method and is mutable; not a variable like INT that isn't mutable.
#     #to change INT we would need to re-assign but can't in python 2 because LEGB
#     def inner(*args):
#         if not remaining:
#             raise ValueError("too many times")
#         #print "REMAINING: {}".format(len(remaining))
#         remaining.pop()
#
#         return f(*args)
#     inner.__doc__ = f.__doc__   # preserve docstring from add function
#     inner.__name__ = f.__name__ # preserve name of function
#     return inner
#
# @maxfive
# def add(a, b):
#     """This is my help: will add 2 things together"""
#     return a + b
#
# print help(add)
#
# for i in range(10):
#     print add(i, i)

###############
# time 3:00
# this following example is often used in Flask, though its hidden mostly
# def max_n_times(n):
#     def deco(f):
#         remaining = list(range(n))
#
#         def inner(*args):
#             if not remaining:
#                 raise ValueError("too many times")
#
#             remaining.pop()
#
#             return f(*args)
#
#         return inner
#     return deco
#
# @max_n_times(7)
# def add(a, b):
#     """This is my help: will add 2 things together"""
#     return a + b
# # this will be a function in a function in a function
# #add = max_n_times(7)(add)
#
# #print help(add)
#
# for i in range(10):
#     print add(i, i)


###########################################
#   BACK TO USING FUNCTIONS WITH DECORATORS
#   TIME 3:17
###########################################
# check to make sure argument sent is the same type
# def onlyallow(a_type):
#     def deco(f):
#         def inner(*args):
#             for one_arg in args:
#                 if type(one_arg) != a_type:
#                     raise TypeError("Argument {} is a {}".format(one_arg, type(one_arg)))
#             return f(*args)
#         return inner
#     return deco
#
#
#
# @onlyallow(str)
# def hello(name):
#     return "Hello, {}".format(name)
#
# @onlyallow(int)
# def mysum(*numbers):
#     total = 0
#     for one_number in numbers:
#         total += one_number
#     return total
#
# print hello('chet')
#
# print hello(5)
#
# print mysum(1,2,3,4,'a')


####
# Time 3:32:30
# check to make sure multiple arguments sent is the same type
# def onlyallow(*allowed_types):
#     def deco(f):
#         def inner(*args):
#             for one_arg in args:
#                 if type(one_arg) not in allowed_types:
#                     raise TypeError("Argument {} is a {}".format(one_arg, type(one_arg)))
#             return f(*args)
#         return inner
#     return deco
#
#
#
# @onlyallow(str, int)        # enter types allowed here: ie str, int, list
# def hello(name):
#     return "Hello, {}".format(name)
#
# @onlyallow(int)
# def mysum(*numbers):
#     total = 0
#     for one_number in numbers:
#         total += one_number
#     return total
#
# print hello('chet')
#
# print hello(5)
#
# print hello([1,2,3])
#
# print mysum(1,2,3,4)


##################################
#   BEST USE OF CHECKING FOR TYPES
#   Time 3:34
##################################
# using isinstance approach
# check to make sure multiple arguments sent is the same type
# def onlyallow(*allowed_types):
#     def deco(f):
#         def inner(*args):
#             for one_arg in args:
#                     if not isinstance(one_arg, allowed_types):
#                         raise TypeError("Argument {} is a {}".format(one_arg, type(one_arg)))
#             return f(*args)
#         return inner
#     return deco
#
# @onlyallow(str, int, tuple, list)        # enter types allowed here: ie str, int, list
# def hello(name):
#     return "Hello, {}".format(name)
#
# @onlyallow(int)
# def mysum(*numbers):
#     total = 0
#     for one_number in numbers:
#         total += one_number
#     return total
#
# print hello('chet')
# print hello(5)
# print hello([1,2,3])
# print mysum(1,2,3,4)

########
# Time 3:40
# adding a new attribute 'xyz' to every new instance
# def add_xyz(c):
#     def inner(*args):
#         new_instance = c(*args)
#         new_instance.xyz = 123
#         return new_instance
#     return inner
#
# @add_xyz
# class Foo(object):
#     def __init__(self, x):
#         self.x = x
#     def x2(self):
#         return self.x * 2
#
# f = Foo(20)
# print vars(f)

#####
# time 3:49
# CREATION: create an attribute that shows when instance/object was created
import time
# def add_ctime(c):
#     def inner(*args):
#         new_instance = c(*args)
#         new_instance.creation = time.time()
#         return new_instance
#     return inner
#
# @add_ctime
# class Foo(object):
#     def __init__(self, x):
#         self.x = x
#
#
# f = Foo(20)
# print vars(f)
# f = Foo(20)
# print vars(f)

####
# Stacking decorators
# import time
# def add_ctime(c):
#     def inner(*args):
#         new_instance = c(*args)
#         new_instance.creation = time.time()
#         return new_instance
#     return inner
#
# def add_xyz(c):
#     def inner(*args):
#         new_instance = c(*args)
#         new_instance.xyz = 123
#         return new_instance
#     return inner
#
# @add_ctime
# @add_xyz
# class Foo(object):
#     def __init__(self, x):
#         self.x = x
#
#
#
# f = Foo(20)
# print vars(f)
# f = Foo(20)
# print vars(f)
