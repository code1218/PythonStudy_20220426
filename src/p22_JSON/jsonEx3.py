import json

json_obj = {
    "id" : 20220001,
    "username" : "Junil",
    "password" : "1234",
    "hobby" : ["축구","농구","골프","테니스"]
}

with open('C:/Users/USER/Desktop/src/', encoding="utf8") as f:
    json_string = json.dump(json_obj,f,indent=4, ensure_ascii=False)
