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


# METHOD THREE - BEST
# taking advantage of zip
# example
# letters = ['a', 'b', 'c']
# numbers = [10, 20, 30]
#
# print zip(letters, numbers)     # returns a list of tuples
#
# # This works too
# letters = 'abc'
# numbers = [10, 20, 30]
# print zip(letters, numbers)     # returns a list of tuples
#
# # here's how to do this with our earlier examples.
# def line_to_dict(one_line):
#     # dict knows how to take a list of tuples and turn into a dictionary!
#     return dict(zip(['brand', 'color', 'size'],
#                     one_line.strip().split('\t')))
#
# shoe_list = [line_to_dict(one_line_shoes)
#              for one_line_shoes in open('shoe-data.txt')]
#
# for s in shoe_list:
#     print s


# SORTING BY SIZE
def line_to_dict(one_line):
    brand, color, size = one_line.strip().split('\t')
    return {'brand': brand,
            'color': color,
            'size': int(size)}

def shoe_size(x):       # key=sort always gets one argument. I think its just in its DNA
    return x['size']


def brand_size(one_shoe):
    return one_shoe['brand'], one_shoe['size']

shoe_list = [line_to_dict(one_line_shoes)
             for one_line_shoes in open('shoe-data.txt')]

# sort by size
shoe_list.sort(key=shoe_size)
for s in shoe_list:
    print s

print "&" * 60
shoe_list.sort(key=brand_size)
for s in shoe_list:
    print s

# same but now with lambda
print "$" * 60
shoe_list.sort(key=lambda x: (x['brand'], x['size']))
for s in shoe_list:
    print s


# But there is a better way using operator
# itemgetter works on anything with [] brackets
print "%&" * 60
import operator
shoe_list.sort(key=operator.itemgetter('brand', 'size'))
for s in shoe_list:
    print s

# another example of itemgetter
words = "This is a bunch of junk".split()
print operator.itemgetter(2,4)(words)

print operator.itemgetter(2,4)(shoe_list)

