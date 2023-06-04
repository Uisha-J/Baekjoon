arr = input().upper()
arr = list(arr)
arrlist = [0] * 26
result = ''
maxcount = 0

for i in range(len(arr)):
    arr[i] = ord(arr[i]) - 65
    arrlist[arr[i]] += 1

for i in range(26):
    if maxcount <= arrlist[i]:
        maxcount = arrlist[i]
        result = chr(i + 65)

arrlist.sort(reverse=True)
if arrlist[0] == arrlist[1]:
    result = '?'

print(result)
