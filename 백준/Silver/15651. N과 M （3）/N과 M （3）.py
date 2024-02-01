import sys

N, M = map(int, sys.stdin.readline().split())

if M == 1:
    for i in range(1, N+1):
        print(i)
elif M == 2:
    for i in range(1, N+1):
        for j in range(1, N+1):
            print(i, j)
elif M == 3:
    for i in range(1, N+1):
        for j in range(1, N+1):
            for k in range(1, N+1):
                print(i, j, k)
elif M == 4:
    for i in range(1, N+1):
        for j in range(1, N+1):
            for k in range(1, N+1):
                for l in range(1, N+1):
                    print(i, j, k, l)
elif M == 5:
    for i in range(1, N+1):
        for j in range(1, N+1):
            for k in range(1, N+1):
                for l in range(1, N+1):
                    for e in range(1, N+1):
                        print(i, j, k, l, e)
elif M == 6:
    for i in range(1, N+1):
        for j in range(1, N+1):
            for k in range(1, N+1):
                for l in range(1, N+1):
                    for e in range(1, N+1):
                        for w in range(1, N+1):
                            print(i, j, k, l, e, w)
elif M == 7:
    for i in range(1, N+1):
        for j in range(1, N+1):
            for k in range(1, N+1):
                for l in range(1, N+1):
                    for e in range(1, N+1):
                        for w in range(1, N+1):
                            for q in range(1, N+1):
                                print(i, j, k, l, e, w, q)