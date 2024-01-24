import sys

N, K = map(int, sys.stdin.readline().split())                       # N, K를 입력받는다.

dong = []                                                           # 입력받은 동전의 종류를 dong 리스트에 넣기 위해서 리스트를 선언해둔다.

for i in range(N):                                                  # dong 리스트에 동전의 종류를 넣는다.
    temp = int(sys.stdin.readline())                                
    if temp <= K:                                                   # 이때 입력받은 K보다 큰 금액의 동전의 종류는 필요가 없으므로 작은 것만 리스트에 넣는다.
        dong.append(temp)

result = 0                                                          # 최소 동전의 개수를 저장하기 위한 result.
temp = len(dong)-1                                                  # 제일 큰 동전부터 세기 위한 인덱스를 저장하는 temp.

while True:                                                         # 가장 큰 금액부터 빼서 최소 동전의 수를 만든다.
    if K >= dong[temp]:                                             # 인덱스를 설정해서 하나씩 빼는 방법으로 하니 시간초과가 발생하여 이를 해결하기 위해 몫을 사용한다.
        temp2 = int(K / dong[temp])                                 # 입력받은 금액보다 작은 최대의 동전의 금액으로 나눠서.
        K = K - temp2 * dong[temp]                                  # 그 몫을 곱해서 빼고.
        result = result + 1 * temp2                                 # 최종 결과에도 몫을 이용하여 개수를 더해준다.
    else:
        temp = temp - 1
    if K == 0 or temp < 0:
        break

print(result)                                                        # 최종 결과 출력!