staff = (input().split())

A = staff[0]
B = staff[1]
walletA = list(map(int,input().split()))
emptywallet = [0]
walletB = emptywallet * int(B)
wallet = walletA + walletB

for _ in range(A):
    M = int(input().split())
    for i in range(A+B):
        wallet[A] = wallet[A] - M[i]
        wallet[i] = wallet[i] + M[i]

print(wallet)