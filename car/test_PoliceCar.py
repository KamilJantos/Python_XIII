from unittest import TestCase

from car.PoliceCar import PoliceCar


class TestPoliceCar(TestCase):
    def setUp(self):
        self.police_car = PoliceCar()


class TestPoliceCarInit(TestPoliceCar):
    def test_test_initial_load(self):
        self.assertEqual(self.police_car.current_guns, 0)


class TestLoad(TestPoliceCar):
    def test_should_not_overload(self):
        self.police_car.add_guns()
        self.assertLessEqual(self.police_car.current_guns, self.police_car.max_guns)

    def test_should_return_zero(self):
        self.police_car.remove_guns()
        self.assertGreaterEqual(self.police_car.current_guns, 0)

    def test_should_current_below_limit_equal_value(self):
        self.police_car.add_guns()
        self.police_car.add_guns()
        self.assertEqual(self.police_car.current_guns, 2)

    def test_verify_max_amount_of_guns(self):
        self.police_car.add_guns()
        self.police_car.add_guns()
        self.police_car.add_guns()
        self.police_car.add_guns()
        self.police_car.add_guns()
        self.assertEqual(self.police_car.current_guns, 4)


    def test_should_return_one(self):
        self.police_car.add_guns()
        self.police_car.add_guns()
        self.police_car.remove_guns()
        self.assertEqual(self.police_car.current_guns, 1)

    def test_incorrect_value_verify(self):
        self.police_car.add_guns()
        self.police_car.add_guns()
        self.police_car.remove_guns()
        self.assertNotEqual(self.police_car.current_guns, 2)
