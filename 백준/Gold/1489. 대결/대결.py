import sys                                              # sys.stdin.readline()을 사용하기 위한 sys import.

N = int(sys.stdin.readline())                           # N 입력받기.

A = list(map(int, sys.stdin.readline().split()))        # 팀 A 입력받기.
B = list(map(int, sys.stdin.readline().split()))        # 팀 B 입력받기.

A.sort()                                                # A 리스트 오름차순 정렬.
B.sort(reverse=True)                                    # B 리스트 내림차순 정렬.

                                                        # 착안점 : 일단 이기는 경우가 가장 포인트를 많이주므로 이기는 경우를 제일 많게 작업을 한 이후에 비기는 경우를 생각해야한다.
                                                        # 이기는 경우를 가장 많게 하려면 A의 가장 작은 값부터 시작해서 비교를 하는데 이때 A의 값보다 작은 값 중에서 가장 큰 값을 B에서 선택해서 싸워야 최선의 상황이 된다.
                                                        # 그리고 B를 내림차순으로 정렬하고 A는 가장 작은 값부터 B는 가장 큰 값부터 하나씩 비교를 해서 A가 이기는 경우를 설정하면
                                                        # A의 가장 작은 값부터 이길 수 있는 수 중 가장 큰 값이랑 싸우게 되므로 이렇게 이기는 경우를 먼저 설정 해준다.

result = 0                                              # 최종결과 result

for i in range(N):                                      # A의 가장 작은 값, 그리고 B의 가장 큰 값 이렇게 비교를 해서 이기는 경우를 가장 많이 만들어준다.
    for j in range(N):                                  # 입력으로 0이 들어오지 않으므로 만약 리스트의 값이 0이라는 것은 이미 싸웠다는 뜻이므로 겹쳐서 최종 결과에 더해지지 않게끔 해준다.
        if A[i] > B[j] and A[i] != 0 and B[j] != 0:
            result = result + 2
            A[i] = 0
            B[j] = 0
            break

for i in range(N):                                      # 이후 이기는 상황을 전부 더해준 뒤에 이제 비기는 경우를 검사해줘야 하는데
    for j in range(N):                                  # 위와 마찬가지로 값이 0인 경우는 이미 싸운 뒤므로 제외해주고 만약 같은 값이라면 아직 대결하지 않은 경우이기 때문에
        if A[i] == B[j] and A[i] != 0 and B[j] != 0:    # 최종결과에 1을 더해주고 값을 0으로 변환시켜준다.
            result = result + 1
            A[i] = 0
            B[j] = 0
            break

print(result)                                           # 최종결과 출력!