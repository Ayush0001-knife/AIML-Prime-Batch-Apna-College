class BankAccount():
      def __init__(self,accNo,name,balance):
            self.accNo=accNo
            self.name=name
            self.balance=balance

      def checkBalance(self):
            print("Your balance is: ",self.balance)

      def deposit(self,amount):
            self.balance+=amount
            print("Your new balance is: ",self.balance)

      def withdraw(self,amount):
            self.balance-=amount
            print("Your new balance is: ",self.balance)      
                        