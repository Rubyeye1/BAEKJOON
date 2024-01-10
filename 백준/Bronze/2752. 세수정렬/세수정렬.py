import sys                                          # sys.stdin.readline 함수를 사용하기 위한 sys import.

L = list(map(int, sys.stdin.readline().split()))

L.sort()


a = L[0]
b = L[1]
c = L[2]

print(a, b, c)
