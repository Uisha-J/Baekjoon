N = int(input())
bloomingrate = float(1/N)
ratelist = []

for i in range(N):
    irate = 1 - ((bloomingrate) * i)
    reversed_rate = irate**-1
    ratelist.append(reversed_rate)

if N == 1:
    print(1)
else:
    print(sum(ratelist))