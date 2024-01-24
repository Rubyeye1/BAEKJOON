import sys

N, K = map(int, sys.stdin.readline().split())                       # N, K를 입력받는다.

dong = []                                                           # 입력받은 동전의 종류를 dong 리스트에 넣기 위해서 리스트를 선언해둔다.

for i in range(N):                                                  # dong 리스트에 동전의 종류를 넣고.
    temp = int(sys.stdin.readline())
    if temp <= K:
        dong.append(temp)

result = 0                                                          # 최소 동전의 개수를 저장하기 위한 result.
temp = len(dong)-1                                                  # 제일 큰 동전부터 세기 위한 인덱스를 저장하는 temp.


while True:                                                         # 가장 큰 금액부터 빼서 최소 동전의 수를 만든다.
    if K >= dong[temp]:
        K = K - dong[temp]
        result = result + 1
    else:
        temp = temp - 1
    if K == 0 or temp < 0:
        break

print(result)                                                        # 최종 결과 출력!