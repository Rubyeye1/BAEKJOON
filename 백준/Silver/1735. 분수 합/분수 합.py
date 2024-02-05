import sys
import math
a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())

tempa = a * d
tempb = b * d
tempc = c * b
tempd = d * b

Bunja = tempa + tempc
Bunmo = tempb

temp = math.gcd(Bunja, Bunmo)
print(int(Bunja / temp), int(Bunmo / temp))