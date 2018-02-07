# TASK 1
# create Person class with attribute name
# make a greet method - hello <name>
# TASK 2
# create class Employee with attribute and emp_id
# don't use a name attribute (tricky). don't override, re-use
# and ability to greet - hello
# DRY. Take advantage of what is in person
# ###########################################

class Person(object):
    def __init__(self, name):
        self.name = name
    def greet(self):
        return "Hello, {}".format(self.name)

p1 = Person('chet')
p2 = Person('connie')
print p1.greet()
print p2.greet()

class Employee(Person):
    def __init__(self, name, emp_id):
        Person.__init__(self, name)
        self.emp_id = emp_id


e1 = Employee('pasta', 100)
e2 = Employee('ray', 101)

print e1.greet()
print e2.greet()
