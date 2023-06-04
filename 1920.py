n = int(input())
firstarr = list(map(int,input().split()))

m = int(input())
secarr = list(map(int,input().split()))

firstarr.sort()
left = 0
right = len(firstarr)-1

for i in range(len(secarr)):
    target = secarr[i]
    K = False
    while left <= right:
        mid = (left + right)//2
        if firstarr[mid] == target:
            print('1')
            K = True
            break
        elif firstarr[mid]>target:
            right = mid-1
        else:
            left = mid+1
    left = 0
    right = len(firstarr)-1
    if K == False:
        print('0')