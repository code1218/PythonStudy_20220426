import uuid
from Repository.UserDao import UserDao
import cryptocode

class UserService:

    def encryptPassword(self, password):
        key = str(uuid.uuid1()).replace("-", "")
        encryptPass = cryptocode.encrypt(password, key)

        return encryptPass, key

    def decryptPassword(self, password, encryptPass, decodeKey):
        return str(cryptocode.decrypt(encryptPass, decodeKey)) == password

    def signup(self, user):
        userDao = UserDao()

        user.password, user.decodeKey = self.encryptPassword(user.password)
        
        userDao.signup(user)
    
    def signin(self, username, password):
        userDao = UserDao()
        user = userDao.getUserByUsername(username)

        if self.decryptPassword(password, user.password, user.decodeKey):
            print("로그인 성공")
        else:
            print("로그인 실패")
        
        input("계속하시려면 아무키나 입력하세요...")