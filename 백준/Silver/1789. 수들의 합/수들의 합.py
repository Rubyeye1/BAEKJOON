S = int(input())

result = 0
for i in range(1, 4294967295):
    if S < i:
        break
    S = S - i
    result = i

print(result)