dan = 0
num = 0
result = 0 

while num < 8:
    dan += 2
    print(f"{dan}단")
    num = 0
    while num < 9:
        num += 1
        result = dan * num
        print(f"{dan} x {num} = {result}")
    print()
    dan -= 1
