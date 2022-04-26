# 변수 score < 입력
# score 가 0 보다 작거나 100 보다 크면 해당 점수는 계산할 수 없습니다.
# 아니라면 A,B,C,D,F 학점을 계산하여 출력

# score = 0;100

# if score > 90:
#     print("A")

#     if score > 80:
#         print("B")
#         if score > 70:
#             print("C")
#             if score > 60:
#                 print("D")
#                 if score > 0:
#                     print("F")

score = int(input("점수를 입력"))

if score > 100 or score < 0:
    print("해당 점수 계산 불가")
elif score > 89:
    print("A학점")
elif score > 79:
    print("B학점")
elif score > 69:
    print("C학점")
elif score > 59:
    print("D학점")
else:
    print("F학점")
    