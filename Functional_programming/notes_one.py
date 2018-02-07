from collections import Counter

# list comprehensions -- list, set, dict
# I have a list, apply an expression and use it in the output list

#ss = raw_input("Enter numbers:")
#print sum([int(x)
#     for x in ss.split()])

#sen = raw_input("enter a sentence: ")
#vowel = [ 'a', 'e', 'i', 'o', 'u']
#for s in sen.split():
#    if s[0] not in vowel:
#        print s[1:] + 'ay'
#    elif s[0] in vowel:
#        print s[1:] + "way"



#print sum([int(one_line)
# for one_line in open('nums.txt')
#       if one_line.strip()])




#print ([one_line.split(":")[0]  # SELECT
#        for one_line in open('linux-etc-passwd.txt')    # FROM
#        if one_line.strip() and not one_line.startswith('#')])  # WHERE (CONDITION)


#print ([one_line.split(":")[-1].strip() # SELECT
#        for one_line in open('linux-etc-passwd.txt')    # FROM
#        if one_line.strip() and not one_line.startswith('#')])  # WHERE (CONDITION)

# SET COMPREHENSION
#print ({one_line.split(":")[-1].strip() # SELECT
#        for one_line in open('linux-etc-passwd.txt')    # FROM
#        if one_line.strip() and not one_line.startswith('#')})  # WHERE (CONDITION)


#c = {one_line.split()[0]                        # SELECT
#        for one_line in open('mini-access-log.txt')}  # WHERE (CONDITION)

#print c

#c = Counter(one_line.split()[0]                        # SELECT
#        for one_line in open('mini-access-log.txt')) # WHERE (CONDITION)

#print
#print c.most_common(3)

#c = {one_line.split()[0]                        # SELECT
#        for one_line in open('shoe-data.txt')}  # WHERE (CONDITION)

#def line_to_dict(one_line):
#    brand, color, size = one_line.strip().split('\t')
#    return {'brand':brand,
#            'color': color,
#            'size': size}


#c = [line_to_dict(one_line)                        # SELECT
#        for one_line in open('shoe-data.txt')] # WHERE (CONDITION)

#for one_show in c:
#    print one_show

#def line_to_dict(one_line):
#    return dict(zip(['brand', 'color', 'size'], one_line.strip().split('\t')))


#c = [line_to_dict(one_line)                        # SELECT
#        for one_line in open('shoe-data.txt')] # WHERE (CONDITION)

#for one_show in c:
#    print one_show

#d = {'a':1, 'b':2, 'c':3}

#print ({v : k
# for k,v in d.items()})

#num = [int (x)
#       for x in raw_input("Enter numbers: ").split()]

#num.sort(key=abs)
#print num

#def size(filename):
#    return len(open(filename).read())

#import glob
#output =  glob.glob("*.txt")
#output.sort(key=size)
#print output
'''
filename = 'shoe-data.txt'

def size(by_size):
    return by_size['brand'], by_size['size']


def line_to_dict(one_line):
    brand, color, size = one_line.strip().split('\t')
    return {'brand': brand,
             'color': color,
             'size': int(size)}

shoes = [line_to_dict(one_line)
         for one_line in open(filename)]

shoes.sort(key=size)

for one_shoe in shoes:
    print one_shoe

# or do this as lambda
# lambda x: x*x  (just expression), often used in sort
'''
'''
print "*******************************************"
print "*******************************************"
print "*******************************************"

import operator

filename = 'shoe-data.txt'

def size(by_size):
    return by_size['brand'], by_size['size']


def line_to_dict(one_line):
    brand, color, size = one_line.strip().split('\t')
    return {'brand': brand,
             'color': color,
             'size': int(size)}

shoes = [line_to_dict(one_line)
         for one_line in open(filename)]

#shoes.sort(key=lambda one_show: (one_show['brand'], one_show['size']))
shoes.sort(key=operator.itemgetter('brand', 'size'))
for one_shoe in shoes:
    print one_shoe
'''

'''
import operator
people = [['chet', 'carello'], ['connie', 'charlier'], ['ray', 'apple']]

people.sort(key=lambda last: (last[1], last[0]))
print people
people.sort(key=operator.itemgetter(1,0))
print people
'''
import operator
def by_value(t):
    return t[1], t[0]
t = {'a': 10, 'b': 5, 'c': 15, 'd': 17, 'e':3, 'f':-5, 'g':-3}
for k, v in sorted(t.items(), key=operator.itemgetter(1,0)):
    print "{}: {}".format(k,v)






