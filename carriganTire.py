from tire import Tire


class CarriganTire(Tire):
    def __init__(self, wearArray):
      self.wearArray = wearArray
      
    def needs_service(self):
         for i in self.wearArray:
            if i >= 0.9:
               return True
            
         return False
            
      