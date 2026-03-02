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

      def withdraw(self, amount):
          if amount > self.balance:
             print("Insufficient balance!")
          else:
             self.balance -= amount
             print("Your new balance is:", self.balance)      
                        

person1=BankAccount(12345,"John Doe",1000)
person1.checkBalance()
person1.deposit(500)
person1.withdraw(200)                        