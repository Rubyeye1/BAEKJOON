N = int(input())
array_list = list(map(int, input().split()))
min = array_list[0]
max = array_list[0]
for i in array_list:
    if i < min:
        min = i
    if i > max:
        max = i
print(min, max)