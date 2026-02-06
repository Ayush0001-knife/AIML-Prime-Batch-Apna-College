f=open("sample.txt","r")
f=open("sample.txt","w")

data = f.read()
print(data)

data=f.readline()
print(data)

f.write("Previous data will be removed.")

f.close()