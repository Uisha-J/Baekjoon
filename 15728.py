N, K = input().split()
share_numcard = list(map(int,input().split()))
team_numcard = list(map(int,input().split()))
Neg = 0
Pos = 0
NegJot = False
PosJot = False

sorted_share_numcard = sorted(share_numcard)
sorted_team_numcard = sorted(team_numcard)

for i in range(len(share_numcard)):
    if share_numcard[i] < 0:
        Neg += 1

for i in range(len(team_numcard)):
    if share_numcard[i] > 0:
        Pos += 1

if Neg == len(share_numcard):
    NegJot = True

if Pos == len(share_numcard):
    PosJot = True

if NegJot == True:
    Neg = 0
    for i in range(len(team_numcard)):
        if team_numcard[i] < 0:
            Neg += 1
    if Neg <= int(K):
        for i in range(int(K)):
            del sorted_team_numcard[0]
        print(sorted_share_numcard[-1] * sorted_team_numcard[0])
    else:
        NegJot = False

if PosJot == True:
    Pos = 0
    for i in range(len(team_numcard)):
        if team_numcard[i] > 0:
            Pos += 1
    if Pos <= int(K):
        for i in range(int(K)):
            del sorted_team_numcard[-1]
        print(sorted_share_numcard[0] * sorted_team_numcard[-1])
    else:
        PosJot = False

if NegJot == False and PosJot == False:
    for i in range(int(K)):
        if sorted_share_numcard[0] * sorted_team_numcard[0] > sorted_share_numcard[-1] * sorted_team_numcard[-1]:
            del sorted_team_numcard[0]
        else:
            del sorted_team_numcard[-1]
    if sorted_share_numcard[0] * sorted_team_numcard[0] > sorted_share_numcard[-1] * sorted_team_numcard[-1]:
        print(sorted_share_numcard[0] * sorted_team_numcard[0])
    else:
        print(sorted_share_numcard[-1] * sorted_team_numcard[-1])