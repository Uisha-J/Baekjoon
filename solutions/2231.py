N = input()
status = False

for i in range(1, int(N)+1):
    const = sum(map(int, str(i)))
    decomp = const + i
    if decomp == int(N):
        print(i)
        status = True
        break
    const = 0
    
if status == False:
    print('0')