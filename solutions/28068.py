import sys
print = sys.stdout.write
input = sys.stdin.readline

n = int(input())
pb = []
mb = []

for i in range(n):
    a, b = map(int,input().split())
    if b-a >= 0:
        pb.append((a,b))
    else:
        mb.append((b,a))

pb = sorted(pb,key = lambda x:(x[0], -x[1]))
mb = sorted(mb,key = lambda x:(-x[0], x[1]))
joy = 0
'''
print(pb)
print(mb)
'''
if len(pb) == 0 or pb[0][0] != 0:
    print('0')
    exit()

for i in range(len(pb)):
    if joy < pb[i][0]:
        print('0')
        exit()
    else:
        joy += pb[i][1] - pb[i][0]

for i in range(len(mb)):
    if joy < pb[i][1]:
        print('0')
        exit()
    else:
        joy -= pb[i][1]
        if joy < 0:
            print('0')
            exit()
        joy += pb[i][0]

if joy >= 0:
    print('1')