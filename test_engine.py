import unittest
from capulet_engine import CapuletEngine
from sternman_engine import SternmanEngine
from willoughby_engine import WilloughbyEngine
class test_engine(unittest.TestCase):
   def test_capulet_engine_needs_service_true(self):
      capuletEngine = CapuletEngine(last_service_mileage=0, current_mileage=30001)
      self.assertTrue(capuletEngine.needs_service())
      
   def test_capulet_engine_needs_service_false(self):
      capuletEngine = CapuletEngine(last_service_mileage=0, current_mileage=30000)
      self.assertFalse(capuletEngine.needs_service())
      
      
   def test_sternman_engine_needs_service_true(self):
      sternmanEngine = SternmanEngine(warning_light_is_on=True)
      self.assertTrue(sternmanEngine.needs_service())
      
   def test_sternman_engine_needs_service_false(self):
      sternmanEngine = SternmanEngine(warning_light_is_on=False)
      self.assertFalse(sternmanEngine.needs_service())
      
   def test_willoughby_engine_needs_service_true(self):
      willoughbyEngine = WilloughbyEngine(current_mileage=60001, last_service_mileage=0)
      self.assertTrue(willoughbyEngine.needs_service())
      
   def test_willoughby_engine_needs_service_false(self):
      willoughbyEngine = WilloughbyEngine(current_mileage=60000, last_service_mileage=0)
      self.assertFalse(willoughbyEngine.needs_service())
      

if __name__ == "__main__":
   unittest.main()