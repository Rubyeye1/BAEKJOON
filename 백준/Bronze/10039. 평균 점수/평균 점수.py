result = 0
for i in range(5):
    a = int(input())
    if a < 40:
        a = 40
    result = result + a

result = result / 5

print(int(result))