from abc import ABC, abstractmethod
from engine import Engine
from battery import Battery
from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self):
        self.engine = Engine
        self.battery = Battery

    @abstractmethod
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()


print("succesfully run")
