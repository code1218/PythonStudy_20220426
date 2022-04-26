# 
# 절대경로(경로 맨 앞에 / 또는 \ 로 시작하는것)

# 상대경로(./ 또는 ../ 또는 생략으로 시작)
# 
strList = ['이름: 김기덕\n','나이: 30\n','주소: 부산 해운대구\n']


f = open('C:/Users/USER/Desktop/src/p15_파일입출력/hello.txt', 'w', encoding='utf8')

f.writelines(strList)
for string in strList:
    f.write(string)
f.close()