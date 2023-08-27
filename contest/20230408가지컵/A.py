n = int(input())
eggplant_list = list(input().split())
m, k = map(int, input().split())
kiwilist = []

for i in range(m):
    made_list = []
    Elist = list(map(int, input().split()))
    for j in range(k):
        made_list.append(eggplant_list[Elist[j]-1])
    if 'P' in made_list:
        kiwilist.append('P')
    else:
        kiwilist.append('W')

if 'W' in kiwilist:
    print('W')
else:
    print('P')
