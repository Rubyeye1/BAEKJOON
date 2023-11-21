N = int(input())
for i in range(N):
    for j in range(N-i-1):
        print(" ", end="")
    for k in range(i+1):
        print("*", end="")
    for l in range(i):
        print("*", end="")
    print()