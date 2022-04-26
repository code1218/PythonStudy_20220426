class User:
    email = ""
    name = ""
    username = ""
    password = ""

    def toString(self):
        return f"""[UserDate]
email: {self.email}
name: {self.name}
username: {self.username}      
        """
      
    def toDict(self):
        userDict = dict()
        userDict["email"] = self.email
        userDict["name"] = self.name
        userDict["username"] = self.username
        return userDict