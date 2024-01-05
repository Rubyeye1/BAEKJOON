n = int(input())                                        # 정수 n을 입력받는다.
for i in range(n):                                      # n번의 케이스를 반복.
    result = 1                                          # 결과로 출력할 result를 1로 설정하고.
    temp = int(input())                                 # 의상의 수를 입력받는다.
    wear = {}                                           # 파이썬의 맵인 딕셔너리를 선언.
    for j in range(temp):                               
        key, value = input().split()                    # 의상의 이름, 의상의 종류를 입력받고.
        if not value in wear:                           # 만약 입력받은 의상의 종류가 처음 들어오는 value값이면 그 의상의 종류를 키로하고 value를 1로 설정한다.
            wear[value] = 1                             # 왜 의상의 이름이 아닌 종류를 키로 설정하냐면 종류 안에서 경우의 수 계산이 이루어져야하기 때문에.
        else:                                           # 만약 입력받은 의상의 종류가 처음 들어오는 value값이 아니면 그 의상의 종류의 개수를 +1 한다.
            wear[value] = wear[value] + 1
    for k in wear.keys():                               # result에 딕셔너리의 키들(의상의 종류)안에서의 의상의 숫자를 + 1한 값(아무것도 입지 않았을때)을 곱한다.
        result = result * (wear[k]+1)
    result = result - 1                                 # 총 계산된 경우의 수에서 모든 의상의 종류를 입지 않았을 경우인 1을 빼준다.
    print(result)                                       # 출력!