from datetime import date
from car import Car
from capulet_engine import CapuletEngine
from sternman_engine import SternmanEngine
from willoughby_engine import WilloughbyEngine
from nubbinBattery import nubbinBattery
from spinderBattery import spinderBattery


class carFactory():

    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = spinderBattery(last_service_date, current_date)
        car = Car(battery, engine)
        return car

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = spinderBattery(last_service_date, current_date)
        car = Car(battery, engine)
        return car

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = spinderBattery(last_service_date, current_date)
        car = Car(battery, engine)
        return car

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = nubbinBattery(last_service_date, current_date)
        car = Car(battery, engine)

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = nubbinBattery(last_service_date, current_date)
        car = Car(battery, engine)
        return car


print("succesfully run")
