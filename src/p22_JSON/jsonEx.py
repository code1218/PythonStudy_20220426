import json

user_json = '''{
    "company" : "kakao",
    "users" : [
        {
        "usercode" : "20220001",
        "username" : "kideok",
        "password" : "1234",
        "name" : "김기덕",
        "email" : rldeok@naver.com"
        },{
        "usercode" : "20220002",
        "username" : "deokki",
        "password" : "4321",
        "name" : "김덕기",
        "email" : rldeok@gmail.com"
        }
    ]
}'''

user_json_obj = json.loads(user_json)

print(user_json_obj)
print(type(user_json_obj))

print(f'회사명: {user_json_obj.get("company")}')
userList = user_json_obj.get("users")
print(f'첫번째 사원의 정보: {userList[0].get("name")}')

print(f'두번째 사원의 정보: {userList[1]}')
