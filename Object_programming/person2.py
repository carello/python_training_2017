class Person(object):
    def __init__(self, name):
        self.name = name

    def greet(self):
        return "Hello, {}".format(self.name)

p1 = Person('chet')
p2 = Person('pasta')

print p1.greet()
print p2.greet()

class Employee(Person):

    def __init__(self, name, id_number):
        Person.__init__(self, name)
        self.id = id_number

e1 = Employee('emp1', 1)
e2 = Employee('emp2', 2)

print e1.greet()
print e2.greet()

