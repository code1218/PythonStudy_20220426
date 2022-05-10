import os

from Repository.UserMst import UserMst
from Service.UserService import UserService

class PageController:

    def index(self):
        selectFlag = True

        os.system('cls')
        print("[사용자 관리 프로그램]")
        print("1. 회원가입")
        print("2. 로그인")
        print("q. 프로그램 종료")
        select = input("메뉴를 선택하세요: ")

        if select == "1":
            self.signup()
        elif select == "2":
            self.signin()
        elif select == "q":
            import time
            for i in range(1, 11):
                os.system('cls')
                print(f"프로그램 종료중...({i}/10)")
                time.sleep(0.05);
            selectFlag = False
        else:
            print("다시 선택하세요.")
            input("계속하시려면 아무키나 입력하세요...")
        return selectFlag

    def signup(self):
        os.system('cls')
        print("[회원가입]")
        email = input("이메일: ")
        name = input("이름: ")
        username = input("사용자이름: ")
        password = input("비밀번호: ")

        user = UserMst()
        user.email = email
        user.name = name
        user.username = username
        user.password = password
        #암호화 <-> 복호화
        userService = UserService()
        userService.signup(user)
        print("회원가입이 완료되었습니다.")
        input("계속 하시려면 아무키나 누르세요...")

    def signin(self):
        pass