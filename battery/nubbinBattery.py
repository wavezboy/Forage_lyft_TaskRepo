from datetime import date
from datetime import datetime
from battery.battery import Battery


class nubbinBattery(Battery):
   def __init__(self,  last_service_date: date,  current_date: date):
      self.last_service_date = last_service_date
      self.current_date = current_date
      
   def needs_service(self):
        return self.last_service_date.replace(year=self.last_service_date.year + 2) < datetime.today().date()