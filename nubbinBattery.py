from datetime import date
from datetime import datetime
from battery import Battery


class nubbinBattery(Battery):
    def __init__(self,  last_service_date: date,  current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        if self.last_service_date.replace(year=self.last_service_date.year + 4 ) < datetime.today().date():
            return True
        else :
            return False

print()