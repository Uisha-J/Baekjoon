n, m, k = map(int, input().split())
homelst = list(map(int, input().split()))
stone = sorted(map(int, input().split()))
dmglst = []

for i in range(k - 1):
    dmglst.append((stone[i], sum(homelst[stone[i] - 1:stone[i + 1] - 1])))
dmglst.append((stone[k - 1], sum(homelst[stone[-1] - 1:])))

dmglst.sort(key=lambda x: (-x[1], x[0]))
dmglst = sorted([x[0] for x in dmglst[:m]])

for x in dmglst:
    print(x)
