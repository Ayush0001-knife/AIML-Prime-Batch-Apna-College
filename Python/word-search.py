word = input("Enter the word to search : ")

with open("sample.txt","r") as f:
      count = 1 
      for line in f:
            if word in line:
                  print("Exists in line ",count)

            count+=1      
            