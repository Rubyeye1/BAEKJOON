a = list(map(int, input().split()))
b = list(map(int, input().split()))

resultA = 0
resultB = 0
for i in range(4):
    resultA = resultA + a[i]
for i in range(4):
    resultB = resultB + b[i]

if resultA >= resultB:
    print(resultA)
else:
    print(resultB)
