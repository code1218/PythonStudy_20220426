marks = (90,25,67,45,80)

count = 0
for score in marks:
    count += 1
    result = "합격" if score > 59 else "불합격"
    print(f"{count}번 학생의 점수는 {score}라서 {result}입니다. ")

print()
count = 0
for score in marks:
    count += 1
    if score %2 == 0:
        continue
    print(f"{count}번 학생의 점수는 {score}이고 짝수입니다")
