from car.Car import Car


class Truck(Car):

    def __init__(self):
        self.current_load = 0
        self.max_load = 100

    def load(self, amount):
        self.current_load += amount
        if self.current_load > self.max_load:
            self.current_load = self.max_load

    def unload(self, amount):
        self.current_load -= amount
        if self.current_load < 0:
            self.current_load = 0
