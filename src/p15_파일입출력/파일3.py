f = open('C:/Users/USER/Desktop/src/p15_파일입출력/hello.txt', 'a', encoding='utf8')
f.write('글을 추가합니다.\n')
f.close()

f = open('C:/Users/USER/Desktop/src/p15_파일입출력/hello.txt', 'r', encoding='utf8')

print(f.read())

f.close()

with open('C:/Users/USER/Desktop/src/p15_파일입출력/hello.txt', 'r', encoding='utf8') as f:
    print(f.read())
# with ~~as f: 들여쓰기 밖으로 벗어나면 자동으로 close 됨 // 밖에서는 file객체를 쓸 수 없다.
