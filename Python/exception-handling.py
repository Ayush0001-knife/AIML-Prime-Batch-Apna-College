try:
      x=int(input(("enter x : ")))
      ans=10/x

except ZeroDivisionError:
      print("Divide by zero is not allowed")

else:
      print("ans : ",ans)