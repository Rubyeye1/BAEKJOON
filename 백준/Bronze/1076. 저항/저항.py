import math
import sys
L = []
for i in range(2):
    temp = input()
    if temp == 'black':
        L.append(0)
    elif temp == 'brown':
        L.append(1)
    elif temp == 'red':
        L.append(2)
    elif temp == 'orange':
        L.append(3)
    elif temp == 'yellow':
        L.append(4)
    elif temp == 'green':
        L.append(5)
    elif temp == 'blue':
        L.append(6)
    elif temp == 'violet':
        L.append(7)
    elif temp == 'grey':
        L.append(8)
    else:
        L.append(9)
while True:
    temp = input()
    if temp == 'black':
        L.append(1)
        break
    elif temp == 'brown':
        L.append(10)
        break
    elif temp == 'red':
        L.append(100)
        break
    elif temp == 'orange':
        L.append(1000)
        break
    elif temp == 'yellow':
        L.append(10000)
        break
    elif temp == 'green':
        L.append(100000)
        break
    elif temp == 'blue':
        L.append(1000000)
        break
    elif temp == 'violet':
        L.append(10000000)
        break
    elif temp == 'grey':
        L.append(100000000)
        break
    else:
        L.append(1000000000)
        break

result = (L[0] * 10 + L[1]) * L[2]
print(result)