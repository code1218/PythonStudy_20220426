import json

class DataBase:
    data = dict()

    def __init__(self):
        try:
            with open("C:/Users/USER/Desktop/src/UserManagement/userdata.json", "r", encoding="utf8") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open("C:/Users/USER/Desktop/src/UserManagement/userdata.json", "w", encoding="utf8") as f:
                json.dump(self.data, f, indent=4)
            with open("C:/Users/USER/Desktop/src/UserManagement/userdata.json", "r", encoding="utf8") as f:
                data = json.load(f)
            
    def getDate(self):
        return self.data      

    def save(self):
        with open("C:/Users/USER/Desktop/src/UserManagerment/userdata.json", "w", encoding="utf8") as f:
                json.dump(self.data, f, indent=4, ensure_ascii=False) 