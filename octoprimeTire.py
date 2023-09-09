
from numpy import array
from tire import Tire

class OctoprimeTire(Tire):
   def __init__(self, wearArray):
      self.wearArray = wearArray
   
   def needs_service(self) -> bool:
      sumOfWear = sum(self.wearArray)
      
      if sumOfWear >= 3:
         return True
      else:
         return False
      