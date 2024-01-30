import sys

N, M = map(int, sys.stdin.readline().split()) # M은 가로 N은 세로.

L = [list(map(str, input())) for _ in range(N)]
result = []

for i in range(N-7):
    for j in range(M-7):
        white = 0
        black = 0

        for k in range(i, i+8):
            for e in range(j, j+8):
                if (k+e) % 2 == 0:
                    if L[k][e] != "W":
                        white = white + 1
                    if L[k][e] != "B":
                        black = black + 1
                else:
                    if L[k][e] != "B":
                        white = white + 1
                    if L[k][e] != "W":
                        black = black + 1
        result.append(white)
        result.append(black)

print(min(result))