import sys

a, b, c, d, e, f = map(int, sys.stdin.readline().split())
if a == 0 and e == 0:
    resultA = int(f / d)
    resultB = int(c / b)
    print(resultA, resultB)
elif b == 0 and d == 0:
    resultA = int(c / a)
    resultB = int(f / e)
    print(resultA, resultB)
elif a == 0:
    resultB = int(c / b)
    resultA = (f - int((e * resultB) / d))
    print(resultA, resultB)
elif b == 0:
    resultA = int(c / a)
    resultB = (f - int((d * resultA) / e))
    print(resultA, resultB)
elif d == 0:
    resultB = int(f / e)
    resultA = (c - int((b * resultB) / a))
    print(resultA, resultB)
elif e == 0:
    resultA = int(f / d)
    resultB = (c - int((a * resultA) / b))
    print(resultA, resultB)
else:
    tempa = e * a
    tempb = e * b
    tempc = e * c
    tempd = b * d
    tempe = b * e
    tempf = b * f

    tempA = tempa - tempd
    tempB = tempc - tempf
    resultA = int(tempB / tempA)
    resultB = int((c - (a * resultA)) / b)

    print(resultA, resultB)
