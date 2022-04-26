import os
from UserManagement.repository.user.User import User

class UserService:
    userRepository = None

    def __init__(self, userRepository):
        self.userRepository = userRepository

    def signup(self):
        os.system('cls')
        print("[회원가입]")
        email = input("이메일: ")
        name = input("이름: ")
        username = input("아이디: ")
        password = input("비밀번호: ")

        user = User()
        user.email = email
        user.name = name
        user.username = username
        user.password = password

        self.userRepository.insertUser(user)
    
    def signin(self):
        os.system('cls')
        print("[로그인]")
        username = input("아이디:")
        password = input("비밀번호:")

        user = self.userRepository.getUserByUsername(username)
        if user != None and user.get("password") == password:
            return user

        return None  
        # if user != None:
        #     if user.get("password") == password:
        #         return user
        #     else:
        #         return None
        # else:
        #     return None

    def showUserAll(self):
        userList = self.userRepository.getUserListAll()
        print("[전체 사용자 조회]")
        for user in userList:        
            self.printUser(user)

    def printUser(self, user):       
        print(
            f"""이메일: {user.get('email')}
이름: {user.get('name')}
아이디: {user.get('username')}"""
        )
        print("-----------------------")