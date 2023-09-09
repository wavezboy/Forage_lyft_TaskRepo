import unittest
from datetime import datetime, date
from  nubbinBattery import nubbinBattery 
from spinderBattery import spinderBattery


class testBattery(unittest.TestCase):
   def test_nubbin_battery_needs_service_false(self):
      today = datetime.today().date()
      last_service_date = today.replace(year= today.year - 3)
      battery = nubbinBattery(current_date=today, last_service_date= last_service_date)
      self.assertFalse(battery.needs_service())
      
   def test_nubbin_battery_needs_service_true(self):
      today = datetime.today().date()
      last_service_date = today.replace(year= today.year - 5)
      battery = nubbinBattery(current_date=today, last_service_date= last_service_date)
      self.assertTrue(battery.needs_service())
      
   def test_splinder_battery_needs_service_true(self):
      today = datetime.today().date()
      last_service_date = today.replace(year= today.year - 5)
      battery = spinderBattery(current_date=today, last_service_date= last_service_date)
      self.assertTrue(battery.needs_service())
      
   def test_splinder_battery_needs_service_false(self):
      today = datetime.today().date()
      last_service_date = today.replace(year= today.year - 2)
      battery = spinderBattery(current_date=today, last_service_date= last_service_date)
      self.assertFalse(battery.needs_service())
   
if __name__== "__main__":
   unittest.main()
   