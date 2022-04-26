def madeGrade(_score,_time):
    i = 0 
    totalScore = 0;
    totalTime = 0;
    while i < len(_score):
        totalTime = totalTime + _time[i]
        if _score[i] == 'A+':
            totalScore = totalScore + (4.5 * _time[i])
        elif _score[i] == 'A':
            totalScore = totalScore + (4.0 * _time[i])
        elif _score[i]== 'B+':
            totalScore = totalScore + (3.5 * _time[i])
        elif _score[i] == 'B':
            totalScore = totalScore + (3.0 * _time[i])
        elif _score[i]== 'C+':
            totalScore = totalScore + (2.5 * _time[i])
        elif _score[i] == 'C':
            totalScore = totalScore + (2.0 * _time[i])
        elif _score[i] == 'D+':
            totalScore = totalScore + (1.5 * _time[i])
        elif _score[i] == 'D':
            totalScore = totalScore + (1.0 * _time[i])
        else:
            totalScore = totalScore + 0
        i = i + 1

    return totalScore, totalTime 

count = 0
subject = list()
score = list()
time = list()

while count < 5:
    score.append(input(f"{count +1 }평점: "))
    time.append(int(input(f"{count +1 }이수 학점: ")))
    count = count + 1

totalScoreAndTotalTime = madeGrade(score,time)
print(f"총 평점은 {totalScoreAndTotalTime[0] / totalScoreAndTotalTime[1]}입니다.")

