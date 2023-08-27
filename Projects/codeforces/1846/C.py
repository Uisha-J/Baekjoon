import copy
import sys
input = sys.stdin.readline
print = sys.stdout.write


for i in range(int(input())):
    n, q, t = map(int, input().split())
    players = []
    player = [0, 0]
    for _ in range(n):
        others = list(map(int, input().split()))
        others.sort()
        if _ == 0:
            player = [0, 0, 1]
        else:
            player = [0, 0]

        if n == 1:
            print('1\n')
            pass
        else:
            dp = [0] * (n)
            dp[0] = copy.copy(others[0])
            for k in range(1, q):
                dp[k] = others[k] + dp[k-1]

            if q == 1:
                player[1] += others[0]
            else:
                for j in range(len(others)):
                    if dp[j] <= t:
                        player[1] += dp[j]
                        player[0] += 1
                    else:
                        break
            players.append(player)
    players = sorted(players, key=lambda x: (-x[0], x[1]))
    for i in range(len(players)):
        if len(players[i]) == 3:
            print(f"{i + 1}\n")
