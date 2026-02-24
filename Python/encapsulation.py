class bankAccount:
      def __init__ (self,name,balance,accNo):
            self.name=name  # public variable  
            self._balance=balance   # protected variable (convention to indicate it should not be accessed directly outside the class)
            self.__accNo=accNo     # private variable (name mangling to prevent direct access)


      def get_accNo(self):    # getter function to access private variable
            return self.__accNo  

      def set_accNo(self,newAccNo):  # setter function to modify private variable
            self.__accNo = newAccNo 

acc1=bankAccount("Ayush",10000,1234567890)
print(acc1.name) 
print(acc1._balance)      
print("Previous Account Number:", acc1.get_accNo())
acc1.set_accNo(9876543210)
print("Updated Account Number:", acc1.get_accNo())