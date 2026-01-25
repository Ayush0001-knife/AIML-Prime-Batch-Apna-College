import os

with open("sample.txt","r") as f:
      data=f.read()
      print(data)
      print(len(data))     



os.remove("delete-files.py")