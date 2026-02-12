import json

cities={
      "Noida":10000000,
      "Delhi":20000000,
      "Kolkata":300000
}

with open("cities.json","w") as f:
      json.dump(cities,f,indent=4,sort_keys=True)

with open("cities.json","r") as f:
      py_obj=json.load(f)
      print("Before : ",py_obj)   

new_city=input("Enter the new city : ")
new_population=int(input("Enter the population of city you entered : ")) 


cities[new_city]=new_population     
with open("cities.json","w") as f:
      json.dump(cities,f,indent=4,sort_keys=True)

with open("cities.json","r") as f:
      py_obj=json.load(f)
      print("After : ",py_obj)   
