while True:
    try:
        a, b, c = input().split()
        if a=='0' and b=='0' and c=='0':
            break
        elif (int(a) ** 2) + (int(b) ** 2) + (int(c) ** 2) == 2 * (max(int(a),int(b),int(c)) ** 2):
             print('right')
        else:
         print('wrong')
    
    except:
        print(max(a,b,c))