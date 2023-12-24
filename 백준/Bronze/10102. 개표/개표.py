V = int(input())

a = input()
a = list(a)

resultA = 0
resultB = 0
for i in range(V):
    if a[i] == "A":
        resultA = resultA + 1
    else:
        resultB = resultB + 1


if resultA > resultB:
    print("A")
elif resultB > resultA:
    print("B")
else:
    print("Tie")