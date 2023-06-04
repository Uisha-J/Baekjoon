import sys
input = sys.stdin.readline
print = sys.stdout.write
people = []
ans = []
for i in range(int(input())):
    people.append(input())

for i in range(int(input())):
    name = input()
    if name in people:
        ans.append(name)

print(name.sort())
