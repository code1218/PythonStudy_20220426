import uuid
from Repository.UserDao import UserDao
import cryptocode

class UserService:

    def encryptPassword(self, password):
        key = str(uuid.uuid1()).replace("-", "")
        encryptPass = cryptocode.encrypt(password, key)

        return encryptPass, key

    def signup(self, user):
        userDao = UserDao()

        user.password, user.decodeKey = self.encryptPassword(user.password)
        
        userDao.signup(user)
    