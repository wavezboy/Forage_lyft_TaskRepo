
import unittest
from carriganTire import CarriganTire
from octoprimeTire import OctoprimeTire


class test_tire(unittest.TestCase):
   def test_carriganTire_needs_service_true(self):
      tire = CarriganTire(wearArray=[0, 1, 0, 0 ])
      self.assertTrue(tire.needs_service())
      
   def test_carriganTire_needs_service_false(self):
      tire = CarriganTire(wearArray=[0, 0, 0, 0 ])
      self.assertFalse(tire.needs_service())
      
      
      
   def test_octoprimeTire_needs_service_true(self):
      tire = OctoprimeTire(wearArray=[0,1,1,1])
      self.assertTrue(tire.needs_service())
      
   def test_octoprimeTire_needs_service_false(self):
      tire = OctoprimeTire(wearArray=[0,1,0,1])
      self.assertFalse(tire.needs_service())
      
      
if __name__ == "__main__":
   unittest.main()