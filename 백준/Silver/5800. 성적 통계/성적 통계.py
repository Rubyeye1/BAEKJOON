K = int(input())

for i in range(K):
    temp = list(map(int, input().split()))
    temp = temp[1:]
    temp.sort()
    Min = temp[0]
    Max = temp[-1]
    Gap = 0
    for j in range(0, len(temp)-1):
        tempGap = temp[j+1] - temp[j]
        if Gap < tempGap:
            Gap = tempGap
    print(f"Class {i + 1}")
    print(f"Max {Max}, Min {Min}, Largest gap {Gap}")