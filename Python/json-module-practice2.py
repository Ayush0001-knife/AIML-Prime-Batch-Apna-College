import json

sample_dict={
      "name":"Kanwal",
      "school":"Notre Dame"
}

with open("data.json","r") as f:
      py_obj=json.load(f)
      print(py_obj)

with open("data.json","w") as f:
      json.dump(sample_dict,f)
