N = int(input())

for i in range(N):
    n, test = input().split()
    n = int(n)
    test_len = len(test)
    for j in range(test_len):
        print(test[j] * n, end="")
    print()