#  s1 = set([1,2,3,4,5,6])
#  s2 = set([4,5,6,7,8,9]) s1 & s2
# & = 교집합을 구할수 잇다 (intersection)
# | = 합집합을 구할수 있다 (union) 엔터위에 슬래쉬
# - = 차집합을 구할수 있다 (difference) 빼기 기호

set1 = {1,2,3,4,5}
set2 = {1,3,5,7,9}

set3 = set1.intersection(set2)
print(set3)

set4 = set1.union(set2)
print(set4)

set5 = set1.difference(set2)
print(set5)