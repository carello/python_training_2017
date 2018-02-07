# using isinstance approach
# check to make sure multiple arguments sent is the same type
def onlyallow(*allowed_types):
    def deco(f):
        print ("in DECO")
        def inner(*args):
            url = ("http://chet.com/"),
            for one_arg in args:
                    if not isinstance(one_arg, allowed_types):
                        raise TypeError("Argument {} is a {}".format(one_arg, type(one_arg)))
            return f(*args)
        return inner
    return deco

@onlyallow(str, int, tuple, list)        # enter types allowed here: ie str, int, list
def hello(name):
    return "Hello, {}".format(name)

# @onlyallow(int)
# def mysum(*numbers):
#     total = 0
#     for one_number in numbers:
#         total += one_number
#     return total

print hello('chet')
#print hello(5)
#print hello([1,2,3])
#print mysum(1,2,3,4)