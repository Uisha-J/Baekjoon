import sys
input = sys.stdin.readline
print = sys.stdout.write

a, b = map(int,input().split())
sitedict = {}

for i in range(a):
    site, pw = input().split()
    sitedict[site] = pw

for i in range(b):
    print(sitedict[input().rstrip()] + '\n')