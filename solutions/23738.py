arr = input().lower()

table = str.maketrans('bhpcyx', 'vnrsuh')
arr = arr.translate(table)
arr = arr.replace('e', 'ye')

print(arr)