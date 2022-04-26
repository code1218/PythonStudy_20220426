class UserRepository:
    
    dataBase = None

    def __init__(self, dataBase):
        self.dataBase = dataBase


    def insertUser(self, user):
        data = self.dataBase.getData()
        data.get("user_mst").append(user)
        self.dataBase.save()

    def gutUserByUsername(self, username):
        data = self.dataBase.getData()
        userList = data.get("user_mst")
        for user in userList:
            if user.get("username") == username:
                return user
           
        return None