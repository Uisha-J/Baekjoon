S = list(input())
T = input()
answer = 0


def makingarray(i, k, A):
    for i in range(len(T) - 1):
        if A.index(T[i]) > A.index(T[k]):
            del A[A.index(T[i])]
            del A[A.index(T[k])]
            makingarray(i+1, k+1, A)
        elif A.index(T[i]) <= A.index(T[k]):
            return


for i in range(len(T)):
    for i in range(len(S)):
        location = S.index(T[i])
