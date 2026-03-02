from abc import ABC,abstractmethod

class Animal(ABC):
      @abstractmethod
      def make_sound():
            pass       #If we want to create an abstract method, we can use the pass statement to indicate that the method is intentionally left empty. This allows us to define the method signature without providing an implementation, which can be useful when we want to enforce that subclasses must implement this method.

class Lion(Animal):
      def make_sound(self):
            print("Roar")

class Cow(Animal):
      def make_sound(self):
            print("Moo")            

lion=Lion()
lion.make_sound()            
cow=Cow()
cow.make_sound()              