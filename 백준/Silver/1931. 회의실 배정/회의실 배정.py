N = int(input())                                        # N을 입력받는다.
R = []                                                  # 회의 시작시간과 끝나는시간을 묶어 입력할 리스트 선언.


for i in range(N):                                      # 시작시간과 끝나는시간을 묶어서 리스트에 입력한다.
    a, b = map(int, input().split())
    R.append([a,b])

R.sort(key=lambda x: (x[1], x[0]))                      # 회의를 가장 많이 수행하려면 끝나는시간이 작아야하고 그 끝나는시간 이후에 최대한 빠르게 다음 회의를 시작해야한다.
                                                        # 그러므로 sort함수를 사용하여 x[1] : 끝나는 시간이 가장 빠른순서대로 정렬하되 x[0] : 끝나는 시간이 같다면 시작하는 시간이 가장 작게 정렬한다.


result = 0                                              # 최종 결과 result.
temp = 0
for i in range(N):                                      # 이후 for문으로 만약 현재 회의의 끝나는 시간이 리스트의 다음 회의의 시작시간보다 작거나 같다면.
    if temp <= R[i][0]:                                 # 리스트의 다음 회의를 시작할 수 있음을 의미하므로 최종결과인 result에 +1을 해주고.
        temp = R[i][1]                                  # temp를 다음 회의의 끝나는 시간으로 바꿔준다.
        result = result + 1

print(result)                                           # 최종 결과 출력.