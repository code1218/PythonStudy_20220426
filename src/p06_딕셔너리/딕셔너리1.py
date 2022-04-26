dir1 = {
    'a': 'python',
    'b': 'java',
    'c': 'c',
    'd': 'html',
    'e': 'css',
    'f': 'javascript',
    'g': 'json',
    'h': [1,2,3,4,5,6,7]
}

hashtag = {
    '맛집' : {'지역' : {
        '기장' : ['얼크니손칼국수', '일등가'],
        '영도' : ['거인왕돈까스', '김밥천국'],
        '서면' : ['삼정타워','먹담'],
        }
        
        },
    '여행' : ['국내여행','해외여행'],
    '카페' : ['스타벅스','컴포즈','이디야']
}

print(dir1)

print(dir1['d'])

print(dir1['h'])

print("맛집출력: " + hashtag['맛집']['지역']['영도'][0])

dir2 = {
    'name' : '김기덕',
    'phone' : '01044600980',
    'email' : 'rldeok@naver.com'
}

print(dir2.keys())

list1 = list(dir2.keys())
print(list1)

list2 = []

list2.append(list1.pop(0))
list2.append(list1.pop(0))
list2.append(list1.pop(0))

print(list1)
print(list2)
print(type(list1))
print(type(list2))

list3 = list(dir2.values())
print(list3)

list4 = list(dir2.items())
print(list4)
print(list4[0][0])

dir2.clear()
print(dir2)

list5 = hashtag.get('운동', '값이 없습니다.')
print(list5[:8])

print('카페' in hashtag)
print('운동' in hashtag)

