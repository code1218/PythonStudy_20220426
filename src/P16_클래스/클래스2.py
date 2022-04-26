# """
#    company
#    model
#    coler

#    showCarInfo()
#      제조사:현대자동차
#      모델: 쏘나타
#      색상: 화이트


# """

class Car:
    company = ""
    model = ""
    coler = ""

    def __init__(self):
      print("생성자 호출됨?")

    def showCarInfo(self):
        print(f"제조사: {self.company}")
        print(f"모델: {self.model}")
        print(f"색상: {self.coler}")

    def test(self, *args):
        for arg in args:
          if str(type(arg)) == "<class' int'>":
              print(f'정수: {arg}')
          elif str(type(arg)) == "<class' str'>":
              print(f'문자열: {arg}')

car1 = Car()

car1.company = "현대자동차"
car1.model = "쏘나타"
car1.coler = "화이트"

car1.showCarInfo()
# car1.showCarInfo("test")
print(car1.company)

car1.test(1,2,3,"4",5,6)