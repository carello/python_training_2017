import operator
import os
from collections import Counter

# aka SQL - SELECT, FROM, WHERE

# PART 0
'''
numbers = range(10)
# OLD method
output = []
for one_number in numbers:
    output.append(one_number * one_number)
print output

# New method
print ([one_number * one_number for one_number in numbers])

# EXAMPLE - converting INT to STR with join
mylist = [10, 20, 30]
print ([str(x) for x in mylist])
print ('*'.join([str(x) for x in mylist]))
newlist = ([str(x) for x in mylist])
print type(newlist)
print newlist

# EXAMPLE - working with words
words = "this is a bunch of words"
print words.capitalize()
print words.title()

print ([one_word.capitalize()
        for one_word in words.split()])
print (' '.join([one_word.capitalize()
                 for one_word in words.split()]))
'''

# PART 0A
'''
numbers = raw_input("Enter numbers: ")
print type(numbers) # this will be STR
ss = numbers.split()
print type(ss)  # this will be a list of strings
print ss

sss = ([int(x)
        for x in numbers.split()])
print type(sss)  # this will be a list of INTs
print sss

print (sum([int(x)
            for x in numbers.split()]))
'''

# PIG LATIN
'''
def plword(word):
    if word[0] in 'aeiou':
        return word + 'way'
    else:
        return word[1:] + word[0] + 'ay'

print plword('python')
print plword('computer')
print plword('elephant')

words = raw_input("Enter some words: ")
print words
print ([plword(one_word)
        for one_word in words.split()])
print (' '.join([plword(one_word)
                 for one_word in words.split()]))
'''


# EXAMPLE 0B
'''
numbers = raw_input('Enter numbers: ')  # enter numbers and letters, this will error
# this won't work if numbers and letters
#print ([int(x)
#        for x in numbers.split()])

# Solution: if user enters numbers and letters - ignore letters
print ([int(x)
        for x in numbers.split()
        if x.isdigit()])
'''

# EXAMPLE 0C
'''
words = raw_input('Enter words: ')
print ([one_word.capitalize()
        for one_word in words.split()
        if one_word[0] not in 'aeiou'])

print (' '.join([one_word.capitalize()
                 for one_word in words.split()
                 if one_word[0] not in 'aeiou']))



f = open('nums.txt')
print f
print ([one_line  # basically same as f.readlines()
        for one_line in f])

print ([int(one_line)
        for one_line in f])

# This version will throw errors
#print ([int(one_line)
#        for one_line in open('nums.txt')])

# Solution
print ([int(one_line)
        for one_line in open('nums.txt')
        if one_line.strip()])
'''

# Nested loops with List Comprehension
def loud_return(x):
    print ("I'm returning {}".format(x))
    return x

def loud_compare(x):
    print ("I'm comparing {}".format(x))
    return x

[loud_return(x)
 for x in range(5)
 if loud_compare(x) % 2]

print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&"

# Vs old way
for x in range(5):
    if loud_compare(x) % 2:
        loud_return(x)


'''
# PART 1
# LIST COMPREHENSION
print sum([int(one_line)                # SELECT
     for one_line in open('nums.txt')   # FROM
     if one_line.strip()])              # WHERE

print ([one_line.split(":")[0]
        for one_line in open('linux-etc-passwd.txt')
        if one_line.strip() and not one_line.startswith('#')])

print ([one_line.split(":")[-1].strip()
        for one_line in open('linux-etc-passwd.txt')
        if one_line.strip() and not one_line.startswith('#')])

# PART 2
# SET COMPREHENSION
print ({one_line.split(":")[-1].strip()
        for one_line in open('linux-etc-passwd.txt')
        if one_line.strip() and not one_line.startswith('#')})

ips = {one_line.split()[0]
     for one_line in open('mini-access-log.txt')}

ips_count = Counter([one_line.split()[0]
     for one_line in open('mini-access-log.txt')])

print ips_count.most_common(5)

# Can remove list comprehension []. Collections takes care of this
ips_count = Counter(one_line.split()[0]
     for one_line in open('mini-access-log.txt'))

print ips_count.most_common(5)


# PART 3 - more COMPREHENSION
print "*" * 80


def line_to_dict(one_line):
    brand, color, size = one_line.strip().split('\t')
    return {'brand': brand,
            'color': color,
            'size': size}

shoes = [line_to_dict(one_line)
         for one_line in open('shoe-data.txt')]

for one_shoe in shoes:
    print one_shoe

# OR to be so cool and complex


def line_to_dictzip(one_line):
    return dict(zip(['brand', 'color', 'size'], one_line.strip().split('\t')))

shoes_zip = [line_to_dictzip(one_line)
             for one_line in open('shoe-data.txt')]

for one_shoe in shoes_zip:
    print one_shoe


# PART 4 - DICT COMPREHENSION. Note DICT an SET Comprehension both use {}
print "*" * 80
d = {'a': 1, 'b': 2, 'c': 3}

print ({k: v for k, v in d.items()})


# LAMBDA
print "*" * 80

filename = 'shoe-data.txt'


def size(by_size):
    return by_size['brand'], by_size['size']


def line_to_dict_3(one_line):
    brand, color, size = one_line.strip().split('\t')
    return {'brand': brand,
            'color': color,
            'size': int(size)}

shoes3 = [line_to_dict_3(one_line)
          for one_line in open(filename)]

shoes3.sort(key=size)

for one_shoe3 in shoes3:
    print one_shoe3

# OR - do a lambda
print "*" * 80
print "LAMBDA"


def line_to_dict_4(one_line):
    brand, color, size = one_line.strip().split('\t')
    return {'brand': brand,
            'color': color,
            'size': int(size)}

shoes4 = [line_to_dict_4(one_line)
          for one_line in open(filename)]

shoes4.sort(key=operator.itemgetter('brand', 'size'))
for one_shoe4 in shoes4:
    print one_shoe4

# Another lambda example
print "MORE LAMBDA"
people = [['chet', 'carello'], ['connie', 'charlier'], ['ray', 'apple']]

people.sort(key=lambda last: (last[1], last[0]))
print people
# do the cool way
people.sort(key=operator.itemgetter(1, 0))
print people

# SORTED
print "&" * 80

t = {'a': 10, 'b': 5, 'c': 15, 'd': 17, 'e': 3, 'f': -5, 'g': -3}

for k, v in sorted(t.items(), key=operator.itemgetter(1, 0)):
    print "{}: {}".format(k, v)
'''