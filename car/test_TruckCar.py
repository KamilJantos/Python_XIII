from unittest import TestCase

from car.TruckCar import Truck


class TestTruck(TestCase):

    def setUp(self):
        self.truck = Truck()


class TestTruckInit(TestTruck):
    def test_test_initial_load(self):
        self.assertEqual(self.truck.current_load, 0)


class TestLoad(TestTruck):
    def test_should_not_overload(self):
        self.truck.load(200)
        self.assertEqual(self.truck.current_load, self.truck.max_load)

    def test_should_current_below_limit_equal_value(self):
        self.truck.load(50)
        self.assertEqual(self.truck.current_load, 50)

    def test_should_return_zero(self):
        self.truck.unload(200)
        self.assertGreaterEqual(self.truck.current_load, 0)

    def test_should_return_one(self):
        self.truck.load(51)
        self.truck.unload(50)
        self.assertGreaterEqual(self.truck.current_load, 1)
