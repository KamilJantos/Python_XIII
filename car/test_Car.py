import unittest

from car.Car import Car


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car()


class TestInit(TestCar):
    def test_initial_speed(self):
        self.assertEqual(self.car.speed, 0)

    def test_initial_odometer(self):
        self.assertEqual(self.car.odometer, 0)

    def test_initial_time(self):
        self.assertEqual(self.car.time, 0)


class TestAccelerate(TestCar):
    def test_accelerate_from_zero(self):
        self.car.accelerate()
        self.assertEqual(self.car.speed, 5)

    def test_multiple_accelerates(self):
        for _ in range(3):
            self.car.accelerate()
        self.assertEqual(self.car.speed, 15)

### TEST DO OBSLUGI PALIWA
    def test_should_not_accelerate_if_tank_empty(self):
        speed_before = self.car.speed
        self.car.fuel = 0
        self.car.accelerate()
        self.assertEqual(speed_before, self.car.speed)

### KLASA TESTOWA_OBSLUGA PALIWA
    class TestBank(TestCar):
        def test_should_reduce_fuel_after_acceleration(self):
            fuel_before = self.car.fuel
            self.car.accelerate()
            self.assertLess(self.car.fuel, fuel_before)

        def test_tanked_car_should_not_exceed_max_bank_capacity(self):
            self.car.tank_car(100)
            self.assertLessEqual(self.car.fuel, self.car.max_fuel)


class TestBrake(TestCar):
    def test_break_once(self):
        self.car.accelerate()
        self.car.brake()
        self.assertEqual(self.car.speed, 0)

    def test_multiple_brakes(self):
        for _ in range(5):
            self.car.accelerate()
            for _ in range(3):
                self.car.brake()
            self.assertEqual(self.car.speed, 10)

    def test_should_not_allow_negative_speed(self):
        self.car.brake()
        self.assertEqual(self.car.speed, 0)

    def test_multiple_brakes_at_zero(self):
        for _ in range(3):
            self.car.brake()
        self.assertEqual(self.car.speed, 0)
