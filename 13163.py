n = int(input())

for i in range(n):
    name = list(input().split())
    del name[0]
    name.insert(0, 'god')
    print("".join(name))
