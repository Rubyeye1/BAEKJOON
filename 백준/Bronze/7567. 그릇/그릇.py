n = input()
n = list(n)
temp = len(n)

result = 10
for i in range(1, temp):
    if n[i] != n[i-1]:
        result = result + 10
    else:
        result = result + 5

print(result)