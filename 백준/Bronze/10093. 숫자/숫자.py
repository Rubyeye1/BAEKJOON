import sys

A, B = map(int, sys.stdin.readline().split())

L = []
if A == B:
    print(0)
elif A < B:
    for i in range(A+1,B):
        L.append(i)

    print(B-A-1)
    print(*L)
elif B < A:
    for i in range(B+1, A):
        L.append(i)

    print(A-B-1)
    print(*L)