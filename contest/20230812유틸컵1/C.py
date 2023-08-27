level = 0
stat = 0
union = []

for i in range(int(input())):
    union.append(int(input()))

union.sort()

for i in range(len(union)):
    if i >= 42:
        break

    lvl = union[i]
    if lvl >= 250:
        stat += 5
    elif 200 <= lvl < 250:
        stat += 4
    elif 140 <= lvl < 200:
        stat += 3
    elif 100 <= lvl < 140:
        stat += 2
    elif 60 <= lvl < 100:
        stat += 1
    level += lvl

print(level, stat)
