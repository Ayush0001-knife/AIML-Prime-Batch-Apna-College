class Student():
      def __init__(self,name,rollNo,marks):
            self.__name=name
            self.__rollNo=rollNo
            self.__marks=marks

      def get_student_info(self):
            print("Name: ",self.__name)
            print("Roll No: ",self.__rollNo)
            print("Marks: ",self.__marks)

      def set_student_info(self,name,rollNo,marks):
            if(marks<0 or marks>100):
                  print("Invalid marks! Please enter a value between 0 and 100.")
            elif(rollNo<=0 or rollNo>1000):
                  print("Invalid roll number! Please enter a positive value less than 1000.")
            else:
                  self.__name=name
                  self.__rollNo=rollNo
                  self.__marks=marks

student1 = Student("Alice", 101, 85)
student1.get_student_info()
student1.set_student_info("Bob", 102, 90)
student1.get_student_info()
student1.set_student_info("Charlie", 103, 110)  # Invalid marks
student1.set_student_info("David", -1, 80)     # Invalid roll number