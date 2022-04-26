class CustomError(Exception):
    def __str__(self):
        return "우리가 만든 예외가 발생했습니다."
# a -> b 로 넘어가려할때 예외처리하여 c 로 넘어가게끔 만듬
number = 0

try:
    if number == 0:
        raise CustomError()
    else:
        print("예외 발생하지 않음")
except CustomError as e:
    print(f"Error 내용: {e}")

print(0xac00)

print(dir(Exception))