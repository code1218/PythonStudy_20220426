numbers = [1,2,3,4,5,6,7,8,9]
numbers2 = [3,2,3,2,3,2,3,2,2]
numbers3 = numbers + numbers2
print(numbers3)
numbers3 
print(numbers3[3])
print(numbers3[5:])


list1_2 = ["문자2", 2, 4.5, [1,2,3,4]]
list1 = [1, "문자1", 3.14, 3, list1_2] 
list2 = ["문자1", "문자2", list1_2]

print(list1[1])

print(list1[2])
print(list1[4][2])

print(list2[2][3][1])

list3 = [1, "10"]

print(list3[0]+int(list3[1]))

list3 = list3 + [2, 5]
print(list3)

del list3[2]
print(list3)

list3 = list3 + [5,6,7,8]
print(list3)

del list3[1:5]
print(list3)

list3.append("안녕")
print(list3)
list3 = list3 + ["안녕"]
print(list3)
list4 = [10,20,30]
list3.append(list4)
print(list3)

#list3.sort() 문자열이 같이 있어 출력불가
#print(list3)
list5 = [1,5,3,6,7,82,4]
list5.sort()
print(list5)
# sort 리스트 정렬
#reverse 리스트 역순
list5.reverse()
print(list5)
#insert 해당값삽입
list5.insert(4,10)
print(list5)

#remove는 해당값제거
list5.remove(10)
print(list5)

list5.pop()
print(list5)
list5.pop(0)
print(list5)