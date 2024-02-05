import sys
import math

N = int(sys.stdin.readline())
result = 0
temp = 1
while True:
    if temp * temp <= N:
        result = result + 1
        temp = temp + 1
    else:
        break
print(result)