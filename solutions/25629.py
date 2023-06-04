N = int(input())
odd = 0
even = 0

array = list(map(int, input().split()))

for i in array:
    if i % 2 == 1:
        odd += 1
    elif i % 2 == 0:
        even += 1

if odd == (even + 1) or odd == even:
    print("1")
else:
    print("0")