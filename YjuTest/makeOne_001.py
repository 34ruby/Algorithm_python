n, k = map(int, input().split())

result = 0

while n >= k :
    while n % k != 0 :
        n -= 1
        result += 1
    n //= k
    result += 1

# n이 k보다 크거나 같을 때
# n이 k로 나누어떨어질때까지 n을 1씩 뺀다
# 나누어떨어지면 나눈다
# n이 k보다 작아지면, n을 단순히 1씩 뺀다. 

while n > 1:
    n -= 1
    result += 1

print(result)