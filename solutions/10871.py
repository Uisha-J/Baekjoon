K = list(map(int,input().split()))
N = K[0]
X = K[1]
answer = []

num = input().split()
for i in range(N):
    if int(num[i]) < X:
        answer.append(num[i])

print(' '. join(answer))