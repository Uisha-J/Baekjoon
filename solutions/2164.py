from collections import deque
deq = deque()

N = int(input())
cardlist = deque([])
for i in range(N):
    cardlist.append(i+1)

while len(cardlist) >= 2:
    cardlist.popleft()
    cardlist.append(cardlist.popleft())

print(*cardlist)
