L = []
for i in range(10):
    a = int(input())
    L.append(a)

L.sort()

average = 0
for i in range(10):
    average = average + L[i]
average = average / 10
average = int(average)
L2 = list(map(str, L))
temp = {}
for i in range(10):
    if L2[i] not in temp:
        temp[L2[i]] = 1
    else:
        temp[L2[i]] = temp[L2[i]] + 1

temp2 = 0
many = 0

for k in temp.keys():
    if temp2 < temp[k]:
        temp2 = temp[k]
        many = k
print(average)
print(many)