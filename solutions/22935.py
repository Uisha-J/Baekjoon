import sys
input = sys.stdin.readline
print = sys.stdout.write

num = []
for i in range(1, 16):
    num.append(bin(i)[2:].zfill(4))
for i in range(14, 1, -1):
    num.append(bin(i)[2:].zfill(4))

for i in range(int(input())):
    call = str(num[(int(input())-1) % 28])
    call = call.replace('1', '딸기')
    call = call.replace('0', 'V')
    print(f"{call}\n")