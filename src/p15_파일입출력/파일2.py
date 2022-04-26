string = ''
string2 = ''
f = open('C:/Users/USER/Desktop/src/p15_파일입출력/hello.txt', 'r', encoding='utf8')
string = f.readline()
string2 = f.readline()
f.close()

print(string, end='')
print(string2, end='')

print('================================')
f = open('C:/Users/USER/Desktop/src/p15_파일입출력/hello.txt', 'r', encoding='utf8')
strList = f.readlines()
strList2 = list()

for string in strList:
    strList2.append(string.replace('\n','')) 
f.close()

print(strList)
print(strList2)
print('================================')
f = open('C:/Users/USER/Desktop/src/p15_파일입출력/hello.txt', 'r', encoding='utf8')
string = f.read()
f.close()
print(string)