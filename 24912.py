import sys
input = sys.stdin.readline

n = int(input())
card_list = list(map(int, input().split()))

for i in range(n):
    if i == 0 and card_list[i] == 0:
        if n == 1:
            card_list[i] = 1
        else:
            card_list[i] = 1
            if card_list[i] == card_list[i+1]:
                card_list[i] = 2

    elif i == n-1 and card_list[i] == 0:
        card_list[i] = 1
        if card_list[i] == card_list[i-1]:
            card_list[i] = 2

    elif card_list[i] == 0:
        card_list[i] = 1
        if card_list[i] == card_list[i-1] or card_list[i] == card_list[i+1]:
            card_list[i] = 2
            if card_list[i] == card_list[i-1] or card_list[i] == card_list[i+1]:
                card_list[i] = 3
                if card_list[i] == card_list[i-1] or card_list[i] == card_list[i+1]:
                    print('-1')
                    sys.exit()

    elif i != n-1 and card_list[i] == card_list[i+1]:
        print('-1')
        sys.exit()

print(*card_list)
