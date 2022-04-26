class 아버지:
    carModel = ""
    carColor = ""

    def showCarInfo(self):
        self.carColor = "그레이"
        print("[차량정보]")
        print((f"차량 모델: {self.carModel}"))
        print((f"차량 색상: {self.carColor}"))

class 자식(아버지):
    def showCarInfo(self):
        self.carColor = "블랙"
        print("[차량정보]")
        print((f"차량 모델: {self.carModel}"))
        print((f"차량 색상: {self.carColor}"))

기덕 = 자식()
기덕.carModel = "K3"
기덕.showCarInfo()

아빠 = 아버지()
아빠.carModel = "제네시스"
아빠.showCarInfo()

