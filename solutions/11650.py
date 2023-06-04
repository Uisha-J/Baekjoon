import sys
input = sys.stdin.readline

location = []

for i in range(int(input())):
    xy = list(map(int, input().split()))
    location.append(tuple(xy))

location.sort(key=lambda x: (x[0], x[1]))

for i in range(len(location)):
    print(*list(location[i]))
