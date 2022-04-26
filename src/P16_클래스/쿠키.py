from multipledispatch import dispatch
class Cookie:
    재료 = ""

    @dispatch()
    def __init__(self):
        pass

    @dispatch(str)
    def __init__(self, 재료):
        self.재료 = 재료
    
    def 재료추가(self, 재료):
        self.재료 = 재료

    def showCookieInfo(self):
        print(f'쿠키정보:{self.재료}맛 쿠키')



초코쿠키 = Cookie()

초코쿠키.showCookieInfo()
초코쿠키.재료추가('초코')
초코쿠키.showCookieInfo()

바나나쿠키 = Cookie('바나나')
바나나쿠키.showCookieInfo()