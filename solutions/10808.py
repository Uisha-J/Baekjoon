ans = [0] * 123
word = input()

for i in range(len(word)):
    ans[ord(word[i])] += 1

print(*ans[97:])
