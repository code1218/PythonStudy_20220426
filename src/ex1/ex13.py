user = dict()
# 강사 list[
# 0 -> 이름 : 김준일, 연락처: 010-9988-1916, 나이: 29, 주소: 동래구
# 1 -> 이름 : 김준이, 연락처: 010-9988-1916, 나이: 30, 주소: 부산진구
# ]
# 학생: list[
# 0 -> 이름 : 한성인, 연락처: 010-5851-8721, 나이: 23, 주소: 부산진구
# 1 -> 이름: 서재효, 연락처: 010-8803-2829, 나이: 25, 주소: 동래구
# ]

# 김준일: {이름 : 김준일, 연락처: 010-9988-1916, 나이: 29, 주소: 동래구}
# 김준이: {이름 : 김준이, 연락처: 010-9988-1916, 나이: 30, 주소: 부산진구}
# 한성인: {이름 : 한성인, 연락처: 010-5851-8721, 나이: 23, 주소: 부산진구}
# 서재효: {이름: 서재효, 연락처: 010-8803-2829, 나이: 25, 주소: 동래구}

user['강사']= list()
user['학생']= list()
print(user)

#user['강사'].append(dict())
user.get('강사').append(dict())
user_dtl1 = user.get('강사')[0]
print(user)

user_dtl1['이름'] = "김준일"
user_dtl1['연락처'] = "010-9988-1916"
user_dtl1['나이'] = "29"
user_dtl1['주소'] = "동래구"
print(user)

user.get('강사').append(dict())
user_dtl2 = user.get('강사')[1]
user_dtl2['이름'] = "김준이"
user_dtl2['연락처'] = "010-9988-1916"
user_dtl2['나이'] = "30"
user_dtl2['주소'] = "부산진구"
print(user)

user['학생'] = list()
user.get('학생').append(dict())
user.get('학생').append(dict())
user_dtl3 = user.get('학생')[0]
user_dtl4 = user.get('학생')[1]

user_dtl3['이름'] = "한성인"
user_dtl3['연락처'] = "010-5851-8721"
user_dtl3['나이'] = "23"
user_dtl3['주소'] = "부산진구"

user_dtl4['이름'] = "서재효"
user_dtl4['연락처'] = "010-8803-2829"
user_dtl4['나이'] = "25"
user_dtl4['주소'] = "동래구"

print(user)

name = user.get('강사')[0].get('이름')
profile = user.get('강사')[0]

print(f"{name}: {profile}")

name = user.get('강사')[1].get('이름')
profile = user.get('강사')[1]

print(f"{name}: {profile}")

name = user.get('학생')[0].get('이름')
profile = user.get('학생')[0]

print(f"{name}: {profile}")

name = user.get('학생')[1].get('이름')
profile = user.get('학생')[1]

print(f"{name}: {profile}")





