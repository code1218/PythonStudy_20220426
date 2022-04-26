#자료구조
#선형(리스트,스택,큐, 데크), 비선형(트리, 그래프)
#스택(last in first out) (LIFO)
list1 = [10,20,30,40,50]
stack1 = []

stack1.append(list1.pop(0))
print(stack1)
stack1.append(list1.pop(0))
print(stack1)
stack1.append(list1.pop(0))
print(stack1)
stack1.append(list1.pop(0))
print(stack1)
stack1.append(list1.pop(0))
print(stack1)

print(stack1.pop())
print(stack1)
print(stack1.pop())
print(stack1)
print(stack1.pop())
print(stack1)
print(stack1.pop())
print(stack1)
print(stack1.pop())
print(stack1)

#큐 (first in first out) (FIFO)
list2 = ["a", "b", "c", "d", "e"]
queue1 = []

queue1.append(list2.pop(0))
print(queue1)
queue1.append(list2.pop(0))
print(queue1)
queue1.append(list2.pop(0))
print(queue1)
queue1.append(list2.pop(0))
print(queue1)
queue1.append(list2.pop(0))
print(queue1)

print(queue1.pop(0))
print(queue1.pop(0))
print(queue1.pop(0))
print(queue1.pop(0))
print(queue1.pop(0))

list3 = ("가","나","다","라","마")
list4 = []
#list3의 가장 뒤에서부터 pop 사용하여 list4에 삽입(Insert)할 때 0번 인덱스 삽입
#list4에서 가장 나중에 들어온 것부터 pop해서 출력
list4.insert(0, list3.pop())
list4.insert(0, list3.pop())
list4.insert(0, list3.pop())
list4.insert(0, list3.pop())
list4.insert(0, list3.pop())

