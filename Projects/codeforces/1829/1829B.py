import sys
input = sys.stdin.readline
print = sys.stdout.write

for _ in range(int(input())):
    k = int(input())
    arr = input().split()
    count = 0
    ans = []
    for i in range(k):
        if arr[i] == '0':
            count += 1
            ans.append(count)
        else:
            count = 0
            ans.append(count)
    answer = max(ans)
    print(str(answer) + '\n')
