import os
from UserRepository.UserDao import UserDao
from db.DBConnection import DBConnectionPy
os.system('cls')

if __name__ == "__main__":
    userDao = UserDao(pool=DBConnectionPy())
    userDao.test()
