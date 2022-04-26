# Bool 자료형 연산 (논리 연산) True = 1 False = 0
# and 연산(곱) : 여러 조건 중에 모두가 성립되어야 실행하는 구조
# True and True > True
# True and False > False
# False and False > False
result1 = (0 > -10) and (100 > 10) and (0 == 0)
print(f"result1의 결과: {result1}")


# or 연산(합) : 여러 조건 중에 하나라도 성립하면 실행하는 구조
# True or True > True
# True or False > True
# False or False > False
result2 = (0 == 1) or (10 > 20) or (30 > 10) # (30>100)
print(f"result2의 결과: {result2}")


# not 연산(부정)
#4의 배수이면서 100의 배수가 아닐 때 또는 400의 배수인것

year = 2000 #True
year = 1999 #False


result3 = (year % 4 == 0 ) and (year % 100 !=0) or (year % 400 == 0) 

print(f"윤년 결과: {result3}")


bool1 = True
bool2 = False

print(bool1)
print(bool2)

print(10 < 5)