A, B, C = map(int,input().split())

temp = [0] * 3
temp[0] = A
temp[1] = B
temp[2] = C


t = 0
if temp[0] >= temp[1]:
    t = temp[0]
    temp[0] = temp[1]
    temp[1] = t

if temp[0] >= temp[2]:
    t = temp[0]
    temp[0] = temp[2]
    temp[2] = t

if temp[1] >= temp[2]:
    t = temp[1]
    temp[1] = temp[2]
    temp[2] = t

print(temp[1])
