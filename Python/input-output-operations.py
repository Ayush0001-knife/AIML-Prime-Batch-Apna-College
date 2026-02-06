f=open("file.txt","r")
f=open("file.txt","w")

data = f.read()
print(data)

data=f.readline()
print(data)

f.write("Previous data will be removed.")
data=f.read()
print(data)