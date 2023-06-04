modset = set()

for i in range(10):
    A = int(input()) % 42
    modset.add(A)

print(len(modset))