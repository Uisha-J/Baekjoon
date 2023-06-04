while True:
    arr = str(input())
    if arr == '0':
        break
    reversedarr = arr[::-1]

    if arr == reversedarr:
        print('yes')
    else:
        print('no')