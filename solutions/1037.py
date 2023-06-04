input()
test = list(map(int,input().split()))
test.sort()
print(test[0] * test[-1])