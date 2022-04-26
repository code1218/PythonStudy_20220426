print('로그인 페이지')
username = input('사용자이름: ')
password = input('비밀번호: ')

userList = list()
with open('C:/Users/USER/Desktop/src/p15_파일입출력/user.txt', 'r', encoding='utf8') as f:
    while True:
        user = f.readline()
        if not user:
            break
    userList.append(user.strip())

loginFlag = False

loginUser = dict()

for user in userList: 
    userDict = eval(user)
    if userDict.get('username') == username and userDict.get('password') == password:
        print(f'{username}계정 로그인 성공')
        loginUser = userDict
        loginFlag = True
        break

if loginFlag == False:
    print('해당 계정으로 로그인 할 수 없습니다')
else:
    _email = loginUser.get('emmail')
    _name = loginUser.get('name')
    _username = loginUser.get('username')
    _password = loginUser.get('password')
    print('\n[사용자 정보')
    print(f'이메일: {_email}')
    print(f'성명: {_name}')
    print(f'사용자이름: {_username}')
    print(f'비밀번호: {_password}')