n = 23170
count = 0


coins = [5000,1000,500, 100, 50, 10]

for coin in coins :
    count += n // coin
    n %= coin
print(count)