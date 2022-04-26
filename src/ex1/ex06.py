from copy import copy
a = [1,3,5,4,2]
a.sort(reverse=True)

b = copy(a)
b.reverse()

print(a)
print(b)

list1 = ['a','b','c']
list2 = list1

print("리스트1:",list1)
print("리스트2:",list2)
list2.pop(0)
print("리스트1: ", list1)
print("리스트2: ", list2)