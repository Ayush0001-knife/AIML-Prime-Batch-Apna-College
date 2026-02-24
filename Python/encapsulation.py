class bankAccount:
      def __init__ (self,name,balance,accNo):
            self.name=name
            self._balance=balance
            self.__accNo=accNo

acc1=bankAccount("Ayush",10000,1234567890)
print(acc1.name) 
print(acc1._balance)      
print(acc1.__accNo)  # This will raise an AttributeError because __accNo is private