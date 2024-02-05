import sys
import math

T = int(sys.stdin.readline())

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())

    temp = math.gcd(A, B)
    result = int((A * B) / temp)
    print(result)