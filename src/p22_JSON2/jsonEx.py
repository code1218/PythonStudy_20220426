import json
from textwrap import indent

json_data = '''{
    "username" : "kideok",
    "password" : "1234"
}
'''

user_data = json.loads(json_data)
print(user_data)
print(type(user_data))
print(user_data.get("username"))\

with open("C:/Users/USER/Desktop/src/userdata.json","w",encoding="utf8") as f:
    json.dump(user_data, f, indent=2, ensure_ascii=False)

with open("C:/Users/USER/Desktop/src/userdata.json","r",encoding="utf8") as f:
    user_data = json.load(f)

print(user_data)

user_data_str = json.dumps(user_data,indent=4)
print(user_data_str)
print(type(user_data_str))