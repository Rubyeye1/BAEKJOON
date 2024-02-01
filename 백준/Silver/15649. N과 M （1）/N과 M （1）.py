import sys

N, M = map(int, sys.stdin.readline().split())
answer = []
def Recursive(temp):
    if temp == M:
        print(' '.join(map(str, answer)))
        return

    for i in range(1, N+1):
        if i in answer:
            continue
        answer.append(i)
        Recursive(temp+1)
        answer.pop()

Recursive(0)