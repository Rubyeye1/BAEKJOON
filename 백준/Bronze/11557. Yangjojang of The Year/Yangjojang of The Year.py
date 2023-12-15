N = int(input())

for i in range(N):
    S = int(input())
    school = []
    number = []
    for j in range(S):
        temp1,temp2 = input().split()
        school.append(temp1)
        number.append(int(temp2))
    max = 0
    temp3 = 0
    for j in range(S):
        if max < number[j]:
            max = number[j]
            temp3 = j
            
    print(school[temp3])
