from controller.AuthController import AuthController
from service.UserService import UserService
from repository.UserRepository import UserRepository
from repository.DataBase import DataBase

dataBase = DataBase()
userRepository = UserRepository(DataBase)
userService = UserService(userRepository)
authControleer = AuthController(userService)
authControleer.index()