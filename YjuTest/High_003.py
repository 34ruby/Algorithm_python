n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1
print(result)

# 0 1 2 에서 for문 끝나고 그다음에 3이 실행
# 그리고 다시 0 1 2 에서 for 문 끝나고 그 다음에 3이 실행
# 실행 되면서는 항상 m -= 1이 실행된다.
# 