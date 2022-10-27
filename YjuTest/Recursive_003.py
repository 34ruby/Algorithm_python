def aa(n) :
    result = 1
    for i in range(1, n+1):
        result *= i
    return result 

print('반복문으로 구현', aa(5))