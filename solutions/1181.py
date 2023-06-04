wordlist = []
for i in range(int(input())):
    wordlist.append(input())

wordlist.sort(key=lambda x:(len(x), x))

print(wordlist)