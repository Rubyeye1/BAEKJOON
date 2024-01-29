import sys                                                                              # sys.stdin.readline()을 사용하기 위한 sys import.

N = int(sys.stdin.readline())                                                           # N이 주어진다.

temp = 665                                                                              # temp를 하나씩 증가시키면서 이 숫자에 666이 연속으로 들어가있는지를 확인할 것이므로 temp 초기값을 지정한다.
result = 0                                                                              # N과 result를 비교함으로써 N번째 종말의 수가 되면 반복문을 그만 둘 것이므로 result 변수를 만들어 놓는다.
resultNum = 0                                                                           # 최종적으로 N번째 종말의 수를 담을 resultNum 변수.

while True:                                                                             # 반복문 실행.

    if N == result:                                                                     # 만약 N과 result가 같은 경우에는 N번째 종말의 수를 찾았다는 의미이므로 break한다.
        break

    else:                                                                               # 같지 않은 경우에는.
        temp = temp + 1                                                                 # temp를 1씩 증가시키고.
        tempList = list(map(int, str(temp)))                                            # temp를 리스트화 시킨 후에.

        for i in range(len(tempList)):                                                  # 인덱스를 이용한 반복문을 실행하여.
            if len(tempList) > i+2:                                                     # 연속된 세개를 확인하여 666이 맞는지 확인해야하므로 검사하는 값이 인덱스를 벗어나는지 먼저 체크해주고.
                if tempList[i] == 6 and tempList[i+1] == 6 and tempList[i+2] == 6:      # 만약 연속된 세 원소가 6이라면.
                    result = result + 1                                                 # 종말의 수 이므로 몇 번째 종말의 수인지 result를 1 증가시켜주고.
                    resultNum = temp                                                    # 그 종말의 수를 resultNum에 담아준다.
                    break

print(resultNum)                                                                        # 최종결과 출력!