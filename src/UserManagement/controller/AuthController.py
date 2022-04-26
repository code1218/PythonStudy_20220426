import os
import time

class AuthController:
    userSerive = None
    principalUser = None

    def __init__(self, userService):
        self.userSerive = userService

    def exit(self):
        print("프로그램 종료중...")
        for i in range(100):
            os.system('cls') #한줄로 나오게끔
            print(f"{i+1} / 100")
            time.sleep(0.05)

    def index(self):
        while True:
            os.system('cls')
            print("[사용자 관리 프로그램]")
            print("1.회원가입")
            print("2.로그인")
            print("q. 프로그램 종료")
            select = input("명령을 선택하세요: ")

            if select == "1":
                self.userSerive.signup()
            elif select == "2":
                self.principalUser = self.userService.signin()
                if self.principalUser == None:
                    select = input("로그인에 실패하였습니다. \n다시 로그인 하시겠습니까?(y/n):")
                    if select != "y":
                        self.exit()
                        break
                else:
                    self.mypage()
            elif select == "q":
               self.exit()
               break           
            else:
                print("해당 명령은 지원하지 않습니다.")
        print("프로그램이 종료되었습니다.")
    
    def mypage(self):
        while True:
            os.system('cls')
            print(f"[마이페이지({self.principalUser.get('username')})]")
            print("1.전체 사용자 조회")
            print("2.프로필 내용 조회")
            print("o.로그아웃")
            select = input("명령을 선택하세요: ")

            if select == "1":
                pass
            elif select == "2":
                pass
            elif select == "o":
                self.principalUser = None
                break
            else:
                print("해당 명령은 지원하지 않습니다.")

