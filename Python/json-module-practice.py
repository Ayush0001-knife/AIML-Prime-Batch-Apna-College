import json

json_str='''{
      "name":"Ayush",
      "college_name":"GNIOT",
      "year":"2",
      "course":"BTECH"
}'''

py_obj={
      "name":"Ayush",
      "college_name":"GNIOT",
      "year":"2",
      "course":"BTECH"
}

print("Type of josn_str before conversion ", type(json_str))
print("Type of py_obj before conversion ", type(py_obj))

py_obj1=json.loads(json_str)
json_str1=json.dumps(py_obj)

print("Type of py_obj before conversion ", type(json_str1))
print("Type of josn_str before conversion ", type(py_obj1))
