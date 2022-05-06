import os
from UserRepository.UserDao import UserDao
from db.DBConnection import DBConnectionPy
os.system('cls')

if __name__ == "__main__":
    userDao = UserDao(pool=DBConnectionPy())
    #userDao.test()

    userList = userDao.getUserAll()
    for user in userList:
        user.toString()

    userDao.getUserByUsername("junil")

    userDao.deleteUserByUsername("aa")

    userList = userDao.getUserAll()
    for user in userList:
        user.toString()