class Store:
      store_name="Ayush General Store"
      store_location="Delhi"
      count=0   # to track the number of products
      
      def __init__(self,name,price):
            self.name=name
            self.price=price
            Store.count+=1

      def display_product(self):
            print(f"Product Name: {self.name}, Product Price: {self.price}")

      @classmethod
      def display_store_info(cls):
            print(f"Store Name: {cls.store_name}, Store Location: {cls.store_location}, Total Products: {cls.count}")      

      @staticmethod
      def calc_discount(price,discount):
            final_price=price-(price*discount/100)
            print(f"Final Price after {discount}% discount: {final_price}")
               

p1=Store("phone",10000)   
p2=Store("laptop",50000)
p3=Store("tablet",20000)   

Store.display_store_info()