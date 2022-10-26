n, m = map(int, input().split())

result = 0

for i in range(n):

    data = list(map(int, input().split()))
    # 길이가 m인 배열에 원소를 넣는다 

    min_value = min(data)
    # data 배열 내의 최소값을 찾는다

    result = max(result, min_value)
    # result와 현 배열의 최소값 중 큰 값을 result로 갱신한다. 
    
print(result)