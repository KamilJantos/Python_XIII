

class Car:
    def __init__(self, speed=0):
        self.speed = speed
        self.odometer = 0
        self.time = 0
        self.fuel = 10
        self.max_fuel = 50

    def say_state(self):
        print("I'm going {} kph!".format(self.speed))

    def accelerate(self):
        if self.fuel > 0:
            self.speed += 5
            self.fuel -= 1

    def brake(self):
        if self.speed < 5:
            self.speed = 0
        else:
            self.speed -= 5

    def step(self):
        self.odometer += self.speed
        self.time += 1

    def average_speed(self):
        return self.odometer / self.time

### ZADANIE 1

    def tank_car(self, amount):
        self.fuel += amount
        if self.fuel > self.max_fuel:
            self.fuel = self.max_fuel


if __name__ == '__main__':
    my_car = Car()
    print("I'm a car!")
    while True:
        action = input("Whar should I do ? [A}ccelerate, "
                       "[B]rake, show [O]dometer, "
                       "or show average [S]peed?").upper()
        if action not in "ABOS" or len(action) != 1:
            print("I don't know how to do that")
            continue
        if action == 'A':
            my_car.accelerate()
        elif action == 'B':
            my_car.brake()
        elif action == 'O':
            print("The car has driven {} "
                  "kilometers".format(my_car.odometer))
        elif action == 'S':
            print("The car's average speed was {} "
                  "kph".format(my_car.average_speed()))
        my_car.step()
        my_car.say_state()
