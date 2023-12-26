a, b = input().split()
c, d = input().split()
e, f = input().split()

resulta = 0
resultb = 0

if a == c:
    resulta = e
elif a == e:
    resulta = c
else:
    resulta = a


if b == d:
    resultb = f
elif b == f:
    resultb = d
else:
    resultb = b

print(resulta, resultb)