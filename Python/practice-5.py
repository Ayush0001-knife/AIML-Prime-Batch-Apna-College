class Vehicle():
      def __init__(self,brand,model):
            self.brand=brand
            self.model=model 

class Car(Vehicle):
      def __init__(self,seats):
            self.seats=seats

class Bike(Vehicle):
      def __init__(self,engine_cc):
            self.engine_cc=engine_cc