a = ''.join(reversed(bin(int(input()))))
print(int(a.rstrip('b0'), 2))
