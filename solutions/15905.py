import sys
input = sys.stdin.readline

score = []
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    score.append((a, b))

score = sorted(score, key=lambda x: (-x[0], x[1]))

chicken = 0
for i in range(5, n):
    if score[i][0] == score[4][0]:
        chicken += 1
    else:
        break

print(chicken)
