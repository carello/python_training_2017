############################
#   BASIC INPUT
############################
# get_nums = raw_input("enter nums by spaces: ")
# print sum([int(one_number)
#            for one_number in get_nums.split()
#            if one_number.isdigit()])

############################
#   PIG LATIN
############################
# def pig(x):
#     if x[0] in 'aeiou':
#         return x + 'way'
#     else:
#         return x[1:] + x[0] + 'ay'
#
# get_sentence = raw_input("Enter a sentence: ")
# print(' '.join([pig(word)
#                 for word in get_sentence.split()]))
################
#
# word = raw_input("enter a sentence: ")
#
# def get_word(ww):
#     return ' '.join([w.capitalize()
#                      for w in ww.split()
#                      if w[0] not in 'aeiou'])
#
# print get_word(word)

###############################
#   PASSWORD FILE
###############################
# time 1:18
# print sum([int(n)
#            for n in open('nums.txt')
#            if n.strip()])
#
# with open('nums.txt') as f:
#     print sum([int(n)
#                for n in f
#                if n.strip() != ''])
#
# ml = [one_line.split(':')[0]
#       for one_line in open('linux-etc-passwd.txt')
#       if one_line.strip() and not one_line.startswith('#')]
#
# for l in ml:
#     print l

###################
# from collections import Counter
#
# c = Counter([one_line.split(':')[-1].strip()
#              for one_line in open('linux-etc-passwd.txt')
#              if one_line.strip() and not one_line.startswith('#')])
#
# for k, v in c.items():
#     print "{:18} : {}".format(k, v * 'X')

#####################
#
# def loud_return(x):
#     print "I'm returning: {}".format(x)
#     return x
# def loud_compare(x):
#     print "I'm comparing: {}".format(x)
#     return x
#
# print [loud_return(x)
#        for x in range(5)
#        if loud_compare(x) % 2 ]


############################
#   SET COMPREHENSIONS
#   TIME - 1:50
############################
# Sets are like dictionaries but without values, just keys. so they must be unique and hashable.

# my_s = set([one_line.split(':')[-1].strip()
#             for one_line in open('linux-etc-passwd.txt')
#             if one_line.strip() and not one_line.startswith('#')])
# print type(my_s)
#
# for s in my_s:
#     print s
#
# my_l = [one_line.split(':')[-1].strip()
#         for one_line in open('linux-etc-passwd.txt')
#         if one_line.strip() and not one_line.startswith('#')]
# print type(my_l)
#
# for l in my_l:
#     print l
#
# my_s = {one_line.split(':')[-1].strip()
#         for one_line in open('linux-etc-passwd.txt')
#         if one_line.strip() and not one_line.startswith('#')}
# print type(my_s)
#
# for s in my_s:
#     print s

# ################
# Time 1:57

# from collections import Counter
# my_l = Counter([ip.split()[0]
#                 for ip in open('mini-access-log.txt')])
#
# my_s = {ip.split()[0]
#         for ip in open('mini-access-log.txt')}
#
# print my_l.most_common(3)
# print my_s
#
# for ip in my_s:
#     print ip
#
# print '66.249.65.38' in my_s

#################
# EXAMPLES
# METHOD ONE
# def line_to_dict(one_line):
#     fields = one_line.strip().split('\t')
#     return {'brand': fields[0],
#             'color': fields[1],
#             'size': fields[2]}
#
# shoe_list = [line_to_dict(one_line_shoes)
#              for one_line_shoes in open('shoe-data.txt')]
#
# for s in shoe_list:
#     print s


# METHOD TWO - BETTER
# def line_to_dict(one_line):
#     brand, color, size = one_line.strip().split('\t')
#     return {'brand': brand,
#             'color': color,
#             'size': size}
#
# shoe_list = [line_to_dict(one_line_shoes)
#              for one_line_shoes in open('shoe-data.txt')]
#
# for s in shoe_list:
#     print s
#


############################
#   DICT COMPREHENSION
#   TIME 2:41
############################
# dicts and sets both use {}. Difference is the colon.
# numbers = xrange(10)
# print ({x: x*x
#         for x in numbers
#         if x % 2})
# Values must be unique, last one wins per below
# d = {'a': 1, 'b': 2, 'c': 3, 'd': 3}
# print ({v: k
#         for k, v in d.items()})

#######################
# from collections import Counter
#
# people = [{'first': 'Chet', 'last': 'Carello','hobbies': ['music', 'yoga']},
#           {'first': 'Ray', 'last': 'Cherie', 'hobbies': ['music', 'space']},
#           {'first': 'Connie', 'last': 'Carello', 'hobbies': ['books', 'yoga']},
#           {'first': 'Pasta', 'last': 'Palumbo', 'hobbies': ['sax', 'hiking']}]
#
# #print people[0]['first']
#
# print ([one_person['first']
#        for one_person in people])
#
# # unigue last names
# print ({one_person['last']
#        for one_person in people})
#
# print ([one_person['hobbies']
#        for one_person in people])
#
# print "*" * 60
# # get number of unique hobbies, need a Counter. need to get data in a flat list
# # need nested list comprehension to do this.
# print ([one_hobby   # result is flat list for each value of hobby
#        for one_person in people  # Step 1: iterate across list of dicts
#        for one_hobby in one_person['hobbies']])  # Step 2: iterate over Step1 list, looking for hobbies
# # can now do a Counter of most popular hobbies
# print (Counter([one_hobby
#        for one_person in people
#        for one_hobby in one_person['hobbies']]))
#
# # can filter with if statements too!
# print ([one_hobby
#        for one_person in people
#         if one_person['last'] == 'Cherie'
#        for one_hobby in one_person['hobbies']
#         if one_hobby == 'space'])  # crazy to do this but nice trick. usually one if level is fine.


###############################################################################
# Time 3:00
# What does comprehensions have to do with functional programming
# SELECT is like map in other languges
# WHERE is like filter languges
# use comprehensions in place of map / filter. map /filter is 'old world'
# FUNCTIONS AS PARAMETERS
# def x(y):
#     return y * 2
# print type(x)   # returns type 'function' object
# def does: creates the object and assigns it to variable x
# functions can be passed into variables of functions ie. def x(some_function)


# def hello(name):
#     return 'hello {}'.format(name)
# print hello('chet')
# print hello([1,2,3])
# print hello({'A': 2, 'B': 4})
# print hello(hello)  # this will return a function!
# # Thus functions are objects and can be passed around
# words = "This is a bunch of words for my Python class".split()
# print words
# words.sort()
# print words     # prints in ASCII order
# words.sort(key=len, reverse=True)     # doesn't use cmp 'old world
# print words
# words.sort(key=str.lower)   # this is sorted without regard to case!
# print words
#
#
# get_nums = [int(x)
#             for x in raw_input('enter numbers: ').split()]
# print get_nums
# get_nums.sort(key=abs)
# print get_nums


##########################
# USING KEY= WITH SORT
# TIME 3:19
##########################
# using key= with a function example
# import glob
#
# def file_size(x):
#     print x
#     return len(open(x).read())
#
#
# print file_size('mini-access-log.txt')     # testing to see file size
#
# my_l = glob.glob('*.txt')
# my_l.sort(key=file_size)
# print my_l


############################
#   LAMBDA
#   TIME 3:50
############################
# lambda is anonymous function. A function without a name
# example: lambda x: x*x (just one expression is allowed

# words = "this is a bunch of words".split()
# words.sort(key=lambda word: word[1:])
# print words
#
# # but better way is itemgetter
# # anything that is in square brackets you can use itemgetter
# import operator
# print operator.itemgetter(2,4)(words)


############################
#   SORTED
#   TIME 4:00
############################
people = [['chet', 'carello'], ['barbie', 'carello'], ['joe', 'palumbo'], ['ray', 'cherie']]
people.sort(key=operator.itemgetter(1, 0))  # remember key is getting a function with people as argument, which then sorts
print people
# OR
people.sort(key=lambda one_peep: (one_peep[1], one_peep[0]))
print people

# we can use sorted. works like sort BUT returns a new list and doesn't modify origianl and runs on any iterable
# we are getting a list back (not changing the dict) and are sorting the list

t = (10, 30, 20)
print sorted(t)

d = {'a': 1, 'b': 2, 'c': 3}
for k, v in sorted(d.items()):
    # remember d.items returns a list of tuples [('a': 1), ('c': 3), ('b':2)]
    # sorted will sort the tuples by k, and output a new list.
    print "{} {}".format(k, v)


print sorted(people)    # will sort on just the keys

tt = [-20, -10, -3, 2, 5, 17]
print sorted(tt)
print sorted(tt, key=abs)
# sort is a method on list; sorted is a built in function

#############
#   EXAMPLE
#############
# Time 4:14
# Define a dict with keys and values
# Make sure values are mixup and numberically
# Use sorted() to print contents of dict (k, v)
# sorted by "VALUE"
# Hint - need sorted and some key (lambda or function)
def by_value(t):
    return t[1], t[0]

def my_sort(stuff):
    for k,v in sorted(stuff.items(), key=by_value):
        print  "{}: {}".format(k,v)

d = {'a':10, 'b':5, 'c':15, 'd':17, 'e':3, 'f':-5, 'g':-3}


my_sort(d)

# an easier way
def my_sort(stuff):
    for k, v in sorted(stuff.items(), key=operator.itemgetter(1,0)):
        print "{}: {}".format(k, v)

my_sort(d)

