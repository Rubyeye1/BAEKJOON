import sys

a = list(map(int, sys.stdin.readline().split()))
result = 0
for i in range(5):
    result = result + a[i] * a[i]

result = result % 10

print(result)