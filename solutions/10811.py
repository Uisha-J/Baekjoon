import itertools

N, M = map(int, input().split())
basket = []

for i in range(M):
    basket.append(i+1)

for k in range(N):
    i, j = map(int, input().split())
    test = list(reversed(basket[i-1:j]))
    left = basket[:i-1]
    right = basket[j:]
    basket = left + test + right

print(basket)
