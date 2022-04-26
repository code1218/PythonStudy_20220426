# number = 0
# result = 5050 0~100까지 1씩 number 를 증가시키면서 result에 더한다.

number = 0
result = 0

while number < 100:
    number += 1
    result += number


print(f"결과: {result}")