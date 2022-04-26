score = [70,60,55,75,95,90,80,80,85,100]
total = 0
avg = 0
for i in score:
    total = total + i
avg = total / len(score)

print(f"평군: {avg}")