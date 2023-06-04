import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pokemonlist = dict()

for i in range(n):
    k = input().rstrip()
    pokemonlist[k] = i + 1

pokemonlist_temp = dict(zip(pokemonlist.values(), pokemonlist.keys()))

for i in range(m):
    test = input().rstrip()
    try:
        test = int(test)
        print(str(pokemonlist_temp[int(test)]))
    except:
        print(str(pokemonlist[test]))
