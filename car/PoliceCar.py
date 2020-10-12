from car.Car import Car


class PoliceCar(Car):

    def __init__(self):
        self.current_guns = 0
        self.max_guns = 4

    def add_guns(self):
        self.current_guns += 1
        if self.current_guns > self.max_guns:
            self.current_guns = self.max_guns

    def remove_guns(self):
        self.current_guns -= 1
        if self.current_guns < 0:
            self.current_guns = 0