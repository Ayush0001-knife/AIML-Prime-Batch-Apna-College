class Employee():
      @abstractmethod
      def calculate_salary():
            pass

class FullTimeEmployee(Employee):
      def __init__(self,monthly_salary):
            self.monthly_salary=monthly_salary

      def calculate_salary(self):
            return self.monthly_salary

class ContractEmployee(Employee):      
      def __init__(self,hourly_rate,hours_worked):
            self.hourly_rate=hourly_rate
            self.hours_worked=hours_worked

      def calculate_salary(self):
            return self.hourly_rate * self.hours_worked

class InternEmployee(Employee):
      def __init__(self,stipend):
            self.stipend=stipend

      def calculate_salary(self):
            return self.stipend          