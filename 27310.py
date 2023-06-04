underbar = 0

emoge = list(input())
emoge.remove(':')
emoge.remove(':')

for i in range(len(emoge)):
    if emoge[i] == '_':
        underbar += 1

print(len(emoge) + 4 + underbar * 5)