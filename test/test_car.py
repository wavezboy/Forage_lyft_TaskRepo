import unittest
from datetime import datetime

from batteries.nubbinBattery import nubbinBattery
from batteries.spinderBattery import spinderBattery
from batteries.battery import Battery

from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine
from engines.engine import Engine


from car import Car
from carFactory import carFactory
from serviceable import Serviceable

import sys
import os


class TestCalliope(unittest.TestCase):
    def test_car_need_service(self):
        today = datetime.today().date()
        engine = CapuletEngine(
            last_service_mileage=40000, current_mileage=70000)
        battery = nubbinBattery(
            current_date=today, last_service_date=today.replace(year=today.year-3))

        car = Car(engine, battery)
        serviceable = car.needs_service()
        self.assertTrue(serviceable)


#     def test_battery_should_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 3)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Calliope(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_battery_should_not_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 1)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Calliope(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())

#     def test_engine_should_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 30001
#         last_service_mileage = 0

#         car = Calliope(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_engine_should_not_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 30000
#         last_service_mileage = 0

#         car = Calliope(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())


# class TestGlissade(unittest.TestCase):
#     def test_battery_should_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 3)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Glissade(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_battery_should_not_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 1)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Glissade(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())

#     def test_engine_should_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 60001
#         last_service_mileage = 0

#         car = Glissade(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_engine_should_not_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 60000
#         last_service_mileage = 0

#         car = Glissade(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())


# class TestPalindrome(unittest.TestCase):
#     def test_battery_should_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 5)
#         warning_light_is_on = False

#         car = Palindrome(last_service_date, warning_light_is_on)
#         self.assertTrue(car.needs_service())

#     def test_battery_should_not_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 3)
#         warning_light_is_on = False

#         car = Palindrome(last_service_date, warning_light_is_on)
#         self.assertFalse(car.needs_service())

#     def test_engine_should_be_serviced(self):
#         last_service_date = datetime.today().date()
#         warning_light_is_on = True

#         car = Palindrome(last_service_date, warning_light_is_on)
#         self.assertTrue(car.needs_service())

#     def test_engine_should_not_be_serviced(self):
#         last_service_date = datetime.today().date()
#         warning_light_is_on = False

#         car = Palindrome(last_service_date, warning_light_is_on)
#         self.assertFalse(car.needs_service())


# class TestRorschach(unittest.TestCase):
#     def test_battery_should_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 5)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Rorschach(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_battery_should_not_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 3)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Rorschach(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())

#     def test_engine_should_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 60001
#         last_service_mileage = 0

#         car = Rorschach(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_engine_should_not_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 60000
#         last_service_mileage = 0

#         car = Rorschach(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())


# class TestThovex(unittest.TestCase):
#     def test_battery_should_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 5)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Thovex(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_battery_should_not_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 3)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Thovex(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())

#     def test_engine_should_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 30001
#         last_service_mileage = 0

#         car = Thovex(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_engine_should_not_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 30000
#         last_service_mileage = 0

#         car = Thovex(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())

if __name__ == '__main__':
    unittest.main()
