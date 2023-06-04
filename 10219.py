T = int(input())
for _ in range(T):
    H, W = input().split()
    H = int(H)
    for i in range(H):
        arr = input()
        print(arr[::-1])