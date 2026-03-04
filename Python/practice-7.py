class Person():
      def __init__(self,name,age=None,address=None):
            self.name=name
            self.age=age
            self.address=address

      def display_info(self):
            print(f"Name: {self.name}")
            print(f"Age: {self.age}")
            print(f"Address: {self.address}")