from datetime import date
from car import Car

class carFactory():

   @staticmethod
   def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
         return current_date, last_service_date, current_mileage, last_service_mileage
   

   @staticmethod
   def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int)-> Car:
        return current_date, last_service_date, current_mileage, last_service_mileage
   
   @staticmethod
   def create__palindrome(current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        return current_date, last_service_date, warning_light_on
   
   @staticmethod 
   def create_e_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
      return current_date, last_service_date, current_mileage, last_service_mileage
   
   @staticmethod
   def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
       return current_date, last_service_date, current_mileage, last_service_mileage
