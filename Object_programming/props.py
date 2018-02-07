class Thermo(object):

    max_temp = 50
    min_temp = 25
    def __init__(self):
        self._temp = 25

    @property
    def temp(self):
        print "\tnow in temp getter method"
        return self._temp

    @temp.setter
    def temp(self, new_temp):
        print "\tnow in setter method"

        # if new_temp > Thermo.max_temp:
        #     raise ValueError("Too hot")
        # if new_temp < Thermo.min_temp:
        #     raise ValueError("Too cold")
        if new_temp > Thermo.max_temp:
            new_temp = Thermo.max_temp
        if new_temp < Thermo.min_temp:
            new_temp = Thermo.min_temp

        self._temp = new_temp

t = Thermo()
print t.temp
t.temp = 100
print t.temp
t.temp = 0
print t.temp