sangduck = int(input())
jungduck = int(input())
haduck = int(input())
c = int(input())
s = int(input())

a = []
b = []

a.append(sangduck)
a.append(jungduck)
a.append(haduck)

b.append(c)
b.append(s)


a.sort()
b.sort()

resultA = a[0]
resultB = b[0]
print(resultA + resultB - 50)