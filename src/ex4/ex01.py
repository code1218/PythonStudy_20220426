# 최대값, 최소값
# num1,num2,num3 정수 3를 입력받는다.
# madeMax(_num1,_num2,_num3)
# madeMin(_num1,_num2,_num3)

# 최대값: 00
# 최소값: 00

def madeMax(_num1,_num2,_num3):
        maxResult = 0
        if _num1 > _num2:
            maxResult = _num1
        else:
            maxResult = _num2
        
        if maxResult < _num3:
            maxResult = _num3

        return maxResult


def madeMin(_num1,_num2,_num3):
        maxResult = 0
        
        if _num1 < _num2:
            maxResult = _num1
        else:
            maxResult = _num2
        
        if maxResult > _num3:
            maxResult = _num3

        return maxResult

num1 = int(input("첫번째 수 입력"))
num2 = int(input("두번째 수 입력"))
num3 = int(input("세번째 수 입력"))

max = madeMax(num1,num2,num3)
min = madeMin(num1,num2,num3)
print(f"최대값: {max}")
print(f"최소값 {min}")
