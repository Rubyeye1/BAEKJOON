import sys

N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
X = int(sys.stdin.readline())

L.sort()

result = 0
start = 0
end = N-1
while start < end:
    temp = L[start] + L[end]
    if temp == X:
        result = result + 1
        start = start + 1
    elif temp < X:
        start = start + 1
    else:
        end = end - 1

print(result)