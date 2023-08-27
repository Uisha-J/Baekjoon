table = [0] * 10

for i in range(5):
    table[int(input())] += 1

print(table)

for i in range(10):
    if table[i] == 1 or table[i] == 3 or table[i] == 5:
        print(i)
        break
