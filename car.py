from abc import ABC, abstractmethod
from engine.engine import Engine
from battery.battery import Battery
from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self):
        self.engine = Engine
        self.battery = Battery
        

    @abstractmethod
    def needs_service(self):
        pass
