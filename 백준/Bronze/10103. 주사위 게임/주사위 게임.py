n = int(input())

chang = 100
sang = 100

for i in range(n):
    a, b = map(int, input().split())
    if a < b:
        chang = chang - b
    elif a > b:
        sang = sang - a
print(chang)
print(sang)