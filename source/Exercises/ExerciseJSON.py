json_string = '{"name": "Alice", "age": 30, "city": "New York"}'

import json

# Parse JSON string to Python dictionary
data = json.loads(json_string)
print(data)
print(type(data))
print(data['name'])
print(data['age'])
print(data['city'])

# Convert Python dictionary to JSON string
data_dict = {
    "name": "Bob",
    "age": 25,
    "city": "Los Angeles"
}

json_data = json.dumps(data_dict)
print(json_data)
print(type(json_data))
print(json_data[0:10])  # Print first 10 characters of JSON string
print(json_data[10:20])  # Print next 10 characters of JSON string

# Pretty-print JSON string
pretty_json = json.dumps(data_dict, indent=4)
print(pretty_json)

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4, separators=(", ", " : "), sort_keys=True))