N = int(input())
for _ in range(N):
    score = 0
    streak = 0
    test = input()
    testlist = list(test)
    for i in range(len(test)):
        if testlist[i] == 'O':
            streak +=1
            score += streak
        else:
            streak = 0
    print(score)