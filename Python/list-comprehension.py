square=[]

for i in range(6):
    square.append(i*i)

sq=[i*i for i in range(6) if i%2 !=0 ]
print(sq)
