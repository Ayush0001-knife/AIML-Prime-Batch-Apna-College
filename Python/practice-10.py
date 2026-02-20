# Write 5 names entered by the user
with open("names.txt", "w") as f:
    for i in range(5):
        name = input("Enter a name: ")
        f.write(name + "\n")

# Read and print all names
with open("names.txt", "r") as f:
    print("Names in file:")
    print(f.read())