import math

for i in range(int(input())):
    arr = input()
    lenarr = len(arr)
    headarr = arr[0:(math.ceil(lenarr/3))]
    tail = headarr[1:]
    tailrev = tail[::-1]
    headrev = headarr[::-1]

    if arr == (headarr + headrev + headarr):
        print(1)
    elif arr == (headarr + headrev[1:] + headarr):
        print(1)
    elif arr == (headarr + headrev + tail):
        print(1)
    elif arr == (headarr + headrev[1:] + tail):
        print(1)
    else:
        print(0)
