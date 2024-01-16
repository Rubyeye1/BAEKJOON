a = input().split("-")                              # a에 -를 기준으로 split해서 식을 입력받는다.

result = 0                                          # 결과값 result를 설정한다.

for i in a[0].split("+"):                           # 위에서 이미 -를 기준으로 나눠놓았기 때문에 먼저 첫번째 -가 나오기 전까지는 다 더한 후에 그 뒤의 값들은 괄호를 쳐서 전부 빼주면 되므로.
    result = result + int(i)                        # -가 나오기 전까지의 값들을 +를 기준으로 나누면 숫자가 되고 이것을 int로 변환시켜서 더해준다.
    
for i in a[1:]:                                     # a[1]이후가 존재한다는 것은 -가 존재한다는 것이므로.
    for j in i.split("+"):                          # 최솟값을 구하려면 결과값에서 이후 나온 숫자들을 계속해서 빼주면 된다.
        result = result - int(j)
        

print(result)                                       # 최종결과 출력.