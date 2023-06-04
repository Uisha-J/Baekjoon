K = input().split(" ")

h = int(K[0])
m = int(K[1])

if m < 45 and h >= 1:
    print(h-1, m + 15)
elif m < 45 and h == 0:
    print(23, m + 15)
else:
    print(h, m-45)