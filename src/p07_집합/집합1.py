set1 = set([1,2,3,4,5])
print(set1)

set1.add(10)
set1.add(113)
set1.add(122)
set1.add(13)
set1.add(10)
print(set1)
# 비선형 (트리, 그래프)
# 기준 10 , 10보다 작으면 왼 크면 오// 정중앙값을 잡은뒤 그 다음 정중앙 값을 찾음
# 파이썬은 트리형태의 값을 지님, 값이 중복되지가 않아야함

set2 = set("안녕하세요")
print(set2)

# seatch = '요'

# list1 = list(set2)
# print(list1[0])

# for value in list1:
#     if value == seatch : 
#         print(value)

#     else:
#         print('해당 값은 존재하지 않습니다')
#         break

#  s1 = set([1,2,3,4,5,6])
#  s2 = set([4,5,6,7,8,9]) s1 & s2
# & = 교집합을 간단히 구할수 잇다
# | = 합집합을 구할수 있다
