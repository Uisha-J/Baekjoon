N = int(input())
yes = 0
no = 0

for i in range(N):
    vote = input()
    if vote == '0':
        no += 1
    else:
        yes += 1

if yes > no:
    print('Junhee is cute!')
if yes < no:
    print('Junhee is not cute!')