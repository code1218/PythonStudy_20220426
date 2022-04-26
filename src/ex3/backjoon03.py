n = int(input("별의 개수: "))
i = 0

while i < n:
    i += 1
    print(" " * (n - i), end='')
    print("*" * i)

i = 0
while i < n:
    i += 1
    print((" " * (n - i)) + ("*" * i))



# i = 0
# while i < n:
#     i += 1
#     print(("" * (n - 1)) + ("*" * i))

i = 0
while i < n:
    i += 1
    print((" " * i) + ("*" * (n-i)))
    i +=1

