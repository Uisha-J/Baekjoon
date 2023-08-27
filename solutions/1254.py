s = input()

for i in range(len(s), 0, -1):
    temp = s[-i:]
    if temp[::-1] == temp:
        ans = len(temp)
        break

print(2 * len(s) - ans)
