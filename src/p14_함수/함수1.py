def lastName(name):
    if name[0] == "김":
        print(f"{name}님은 김씨입니다.")
    else:
        print(f"{name}님은 김씨가 아닙니다.")




names = ["김준일","강주현","이영헌","서현준","박노진","송지한","김예진","서재효"]



for name in names:
    lastName(name)
# 입출력이 모두 있는 함수
def add(x, y):
    return x + y
result = add(10,20)

print(result)

# 입력값이 없는 함수
def say():
    return "Hi"

print(say())

# 출력값이 없는 함수
def show(str):
    print(str)

test1 = show("출력값이 없는 함수")
print(test1)


# 입출력 모두 없는 함수
def printInfo():
    print("이름")

test2 = printInfo()
print(test2)

