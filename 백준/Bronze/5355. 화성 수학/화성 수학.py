n = int(input())

for i in range(n):
    res = []
    res = input().split()
    temp = float(res[0])
    lens = len(res)
    for j in range(1, lens):
        if res[j] == "@":
            temp = temp * 3
        elif res[j] == "%":
            temp = temp + 5
        else:
            temp = temp - 7
    print("{:.2f}".format(temp))