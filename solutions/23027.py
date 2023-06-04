arr = input()

if 'A' in arr:
    arr = arr.replace('B', 'A')
    arr = arr.replace('C', 'A')
    arr = arr.replace('D', 'A')
    arr = arr.replace('F', 'A')
elif 'A' not in arr and 'B' in arr:
    arr = arr.replace('C', 'B')
    arr = arr.replace('D', 'B')
    arr = arr.replace('F', 'B')
elif 'A' not in arr and 'B' not in arr  and 'C' in arr:
    arr = arr.replace('D', 'C')
    arr = arr.replace('F', 'C')
elif 'A' not in arr and 'B' not in arr  and 'C' not in arr:
    arr = 'A' * len(arr)

print(arr)