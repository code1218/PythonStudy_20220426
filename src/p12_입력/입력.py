# name = input("이름을 입력해주세요: ")

# print(f"출력확인: {name}")

#
# 숫자 2개를 입력받아서 산술연산자 전부 사용해보기
# num1, num2 
# 덧셈, 뺼셈, 곱셉, 나눗셈, 제곱, 몫, 나머지
#
num1 = int(input("첫번째 수를 입력"))
num2 = int(input("두번째 수를 입력"))

print(f"덧셈: {num1+num2}")
print(f"뺄셈: {num1-num2}")
print(f"곱셈: {num1*num2}")
print(f"나눗셈: {num1/num2}")
print(f"제곱: {num1**num2}")
print(f"몫: {num1%num2}")
print(f"나머지: {num1//num2}")