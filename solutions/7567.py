bowl = list(input())
high = 0

if bowl[0] == '(':
    high += 10
    flip = True
if bowl[0] == ')':
    high += 10
    flip = False

for i in range(len(bowl) - 1):
    if bowl[i+1] == '(' and flip == True:
        high += 5
        flip = True
    elif bowl[i+1] == ')' and flip == True:
        high += 10
        flip = False
    elif bowl[i+1] == '(' and flip == False:
        high += 10
        flip = True
    elif bowl[i+1] == ')' and flip == False:
        high += 5
        flip = False

print(high)