import math

N, num1, num2 = map(int, input().split())
round = 0
distance = abs(num1 - num2)
last_battle = False


def checkround(k):
    global last_battle
    checkround_round = 0
    while last_battle == False:
        k = math.ceil(k / 2)
        checkround_round += 1
        if k == 1:
            last_battle = True
    return checkround_round
