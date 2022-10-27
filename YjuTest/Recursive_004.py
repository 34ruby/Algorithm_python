def ss(n):
    if n <= 1:
        return 1
    return n * ss(n-1)

print('재귀', ss(5))


# 5 * ss(4)
# 5 * 4 * ss(3)
# 5 * 4 * 3 * ss(2)
# 5 * 4 * 3 * 2 * ss(1)
# 5 * 4 * 3 * 2 * 1 
