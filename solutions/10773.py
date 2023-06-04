import sys
n = int(sys.stdin.readline())
call_list = []

counter = 0
for i in range(n):
    money = int(sys.stdin.readline())
    if money == 0:
        del call_list[-1]
    else:
        call_list.append(money)
        counter += 1

print(sum(call_list))
