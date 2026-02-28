class Employee:
      start_time="9am"
      end_time="5pm"

      def change_time(self,end):
            self.end_time=end

class Teacher(Employee):
      def __init__(self,name,subject):
            self.name=name
            self.subject=subject

class AdminStaff(Employee):
      def __init__(self,name,department):
            self.name=name
            self.department=department

class Accountant(AdminStaff):
      def __init__(self,name,department,accounting_software):
            super().__init__(name,department)  # Call the constructor of AdminStaff
            self.accounting_software=accounting_software

t1=Teacher("Alice","Math")
t1.change_time("4pm")  # Changing end time for Teacher
t2=Teacher("Charlie","Science")
a1=AdminStaff("Bob","HR")
ac1=Accountant("David","Finance","QuickBooks")

print(f"{t1.name} teaches {t1.subject} and works from {t1.start_time} to {t1.end_time}.")
print(f"{t2.name} teaches {t2.subject} and works from {t2.start_time} to {t2.end_time}.")
print(f"{a1.name} works in {a1.department} and works from {a1.start_time} to {a1.end_time}.")