from multipledispatch import dispatch
class User:
    username = ""
    password = ""
    name = ""

#  @ >> 어노테이션.디스패치
    @dispatch(str)
    def addUser(self, username):
        self.username = username
    
    @dispatch(str,str)
    def addUser(self, username, password):
        self.username = username
        self.password = password
        
    @dispatch(str,int)
    def addUser(self, username, password):
        self.username = username
        self.password = password

    @dispatch(str,str,str)
    def addUser(self, username, password, name):
        self.username = username
        self.password = password
        self.name = name

    @dispatch(str,int,str)
    def addUser(self, username, password, name):
        self.username = username
        self.password = password
        self.name = name       

    def showUserInfo(self):
        print(f"username:{self.username}")
        print(f"password:{self.password}")
        print(f"name:{self.name}")

user1 = User()
user1.addUser("kideok")
user1.showUserInfo()

user2 = User()
user2.addUser("kideok", 1234)
user2.showUserInfo()

user3 = User()
user3.addUser("kideok", "3214", "김기덕")
user3.showUserInfo()