k = int(input())
equation = list(map(int, input().split()))

if equation[0] * k + equation[1] == equation[2] * k + equation[3]:
    print('Yes', equation[0] * k + equation[1])
else:
    print('No')
