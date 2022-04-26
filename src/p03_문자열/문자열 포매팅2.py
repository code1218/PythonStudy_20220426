str1 = "첫번째 수 {0} 두번째 수 {1} 두수의 합 {2}".format(10,20,10+20)
print(str1)

num1 = 10
num2 = 20
num3 = num1 + num2

str2 = "첫번째 수 {0} 두번째 수 {1} 두수의 합 {2}".format(num1, num2, num3)
print(str2)

str3 = "첫번째 수 {num1} 두번째 수 {num2} 두수의 합 {num2}".format(num1 = 10, num2 = 20, num3 = 10 + 20)
print(str3)

str4 = "문자열 포매팅 정렬 ㅣ{0:^10}ㅣ".format("김기덕")
print(str4)

str5 = "문자열 포매팅 정렬 ㅣ{0:@^10}ㅣ".format("김기덕")
print(str5)

str6 = "문자열 포매팅 정렬 ㅣ{0:@^10.4f}ㅣ".format("김기덕")


str7 = "문자열 포매팅 {0} {{기덕}}". format("김")
print(str7)
