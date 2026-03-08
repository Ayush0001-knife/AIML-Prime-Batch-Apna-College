try:
      x=int(input(("enter x : ")))
      ans=10/x

except ZeroDivisionError:
      print("Divide by zero is not allowed")

except ValueError:
      print("Invalid Input")

else:
      print("ans : ",ans)

finally:  # this will run even if exception is throwed or not 
      print("Program Completed")      