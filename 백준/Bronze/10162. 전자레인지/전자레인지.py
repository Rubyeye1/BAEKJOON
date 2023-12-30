T = int(input())

temp1 = 0
temp2 = 0
temp3 = 0

if T >= 300:
    while (T >= 300):
        T = T - 300
        temp1 = temp1 + 1
        

if T >= 60:
    while (T >= 60):
        T = T - 60
        temp2 = temp2 + 1
        

if T >= 10:
    while (T >= 10):
        T = T - 10
        temp3 = temp3 + 1
        


if (T / 10) != 0:
    print("-1")
else:
    print(f'{temp1} {temp2} {temp3}')