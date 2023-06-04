N = int(input())

for _ in range(N):
    life = input()
    life = life.replace(' ', '')
    score = 0
    for i in range(len(life)):
        score += ord(life[i])-64
    if score == 100:
        print('PERFECT LIFE')
    else:
        print(score)
        