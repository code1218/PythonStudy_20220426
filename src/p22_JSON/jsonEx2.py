import json

with open('./C:\Users\USER\Desktop\src\company.json', encoding="utf8") as f:
    json_obj = json.load(f)

print(json_obj)
print(type(json_obj))