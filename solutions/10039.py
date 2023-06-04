score = []

for i in range(5):
    n = int(input())
    if n < 40:
        score.append(40)
    else:
        score.append(n)

print(sum(score) // 5)
