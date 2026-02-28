class Teacher:
      def __init__(self,salary):
            self.salary=salary

class Student:
      def __init__(self,gpa):
            self.gpa=gpa

class TeachingAssistant(Teacher,Student):
      def __init__(self,name,salary,gpa):
            self.name=name    
            Teacher.__init__(self,salary)  # Initialize Teacher part
            Student.__init__(self,gpa)      # Initialize Student part

ta1=TeachingAssistant("Eve",50000,3.8)
print(f"{ta1.name} is a teaching assistant with a salary of ${ta1.salary} and a GPA of {ta1.gpa}.")