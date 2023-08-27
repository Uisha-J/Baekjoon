lst = []

for i in range(9):
    lst.append(int(input()))

for i in range(9):
    for j in range(i + 1, 9):
        if sum(lst) - (lst[i] + lst[j]) == 100:
            lst[i] = lst[j] = 0
            print(*sorted(lst)[2:])
            exit()
