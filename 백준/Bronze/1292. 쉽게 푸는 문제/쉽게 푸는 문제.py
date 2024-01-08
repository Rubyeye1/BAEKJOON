a = [0 for i in range(1001)]

temp = 1
for i in range(1, 1001):
    if temp > 1000:
        break
    for j in range(i):
        if temp > 1000:
            break
        a[temp] = i
        temp = temp + 1

A, B = map(int, input().split())
result = 0
for k in range(A,B+1):
    result = result + a[k]

print(result)