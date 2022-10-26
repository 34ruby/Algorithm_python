n = 5
m = 8
k = 3

data = [2, 4, 5, 4, 6]

data.sort(reverse=True)

first = data[0]
second = data[1]

secondAdd = m // k

firstAdd = m - secondAdd

result = (firstAdd*first) + (secondAdd*second)

print(result)