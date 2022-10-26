n = 2430

count = 0

coinList = [500, 100, 50, 10]

for coin in coinList:
    count += n // coin
    n = n % coin
    print(coin, count, n)

print(count)