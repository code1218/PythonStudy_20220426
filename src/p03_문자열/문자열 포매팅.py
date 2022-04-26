name1 = "김기덕1"
name2 = "김기덕2"

str1 = "안녕하세요. %-10s 입니다." % name1
str2 = "반갑습니다. %10s 입니다." % name2
print(str1)
print(str2)

str3 = "두 사람의 이름은 %s와 %s 입니다." % (name1, name2)
print(str3)

fNum = 3.4213322
print("실수: %-10.4f " % fNum)
print("실수: %10.4f " % fNum)

