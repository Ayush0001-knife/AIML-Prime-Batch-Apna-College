class Laptop:
      storageType='SSD'

      def __init__(self,ram,storage):
            self.ram=ram
            self.storage=storage

      def get_storage_type(cls):
            print(f"Storage type is {cls.storageType}.")

      def get_info(self):
            print(f"Laptop has {self.ram} GB RAM and {self.storage} GB {self.storageType}.")      


l1=Laptop(16,512)
l2=Laptop(8,256)  

l1.get_info()
l2.get_info()