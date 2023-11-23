arr1 = [list(map(int, input().split())) for _ in range(5)]
arr2 = [0]*5

for num1 in range(5):
    sum = 0
    for num2 in range(4):
        sum = sum + arr1[num1][num2]
    arr2[num1] = sum
max = 0
maxidx = 0
for i in arr2:
    if i > max:
        max = i
for i in range(5):
    if max == arr2[i]:
        maxidx = i + 1 
print(maxidx, max)

