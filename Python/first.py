class Laptop:
      storageType='SSD'

      def __init__(self,ram,storage):
            self.ram=ram
            self.storage=storage

       
      @classmethod
      def get_storage_type(cls):
            print(f"Storage type is {cls.storageType}.")

      def get_info(self):
            print(f"Laptop has {self.ram} GB RAM and {self.storage} GB {self.storageType}.")   

      @staticmethod
      def calc_discount(price,discount):
            final_price=price-(price*discount/100)
            print(f"Final price after {discount}% discount is: {final_price}")         


l1=Laptop(16,512)
l2=Laptop(8,256)  

l1.get_storage_type