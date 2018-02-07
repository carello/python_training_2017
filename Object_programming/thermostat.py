class Thermostat(object):
    max_temp = 50
    min_temp = 25
    def __init__(self):
        self.temp = 25

    def set_temp(self, new_temp):
        print "*" * 60
        if new_temp < self.min_temp:
            raise ValueError("Too low")
        if new_temp > self.max_temp:
            raise ValueError("Temp to high")
        else:
            self.temp = new_temp

    def get_temp(self):
        return self.temp

t = Thermostat()
print t.get_temp()
t.set_temp(4)
print t.get_temp()
#t.set_temp(45)
#t.set_temp(26)

