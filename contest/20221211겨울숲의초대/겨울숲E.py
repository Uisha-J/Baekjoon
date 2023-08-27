type = int(input())
flowerneed = []
ratelist = []

for i in range(type):
    flower, bloomingrate = map(int, input().split())
    flowerneed.append(flower)
    ratelist.append(bloomingrate)


print(flowerneed)
print(ratelist)
print(expected(1))
