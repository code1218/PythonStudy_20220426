



user = dict()
userList = list()

i = 0

while i < 2:
    user = dict()
    email = input('이메일:')
    name = input('성명:')
    username = input('사용자이름:')
    password = input('비밀번호:')

    user['email']= email
    user['name']= name
    user['username']= username
    user['password']= password

    userList.append(str(user))
    userList.append('\n')
    i += 1

print(userList)

with open('C:/Users/USER/Desktop/src/p15_파일입출력/user.txt', 'a', encoding='utf8') as f:
    f.writelines(userList)
