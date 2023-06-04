K = input().split()
if int(K[0]) > int(K[1]):
    print(">")
elif int(K[0]) < int(K[1]):
    print("<")
else:
    print("==")