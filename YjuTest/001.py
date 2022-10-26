# •
# 최적의 해를 빠르게 구하기 위해서는 가장 큰 화폐 단위부터 돈을 거슬러 주면 됩니다
# •
# N 원을 거슬러 줘야 할 때 가장 먼저 500 원으로 거슬러 줄 수 있을 만큼 거슬러 줍니다
# •
# 이후에 100 원 50 원 10 원짜리 동전을 차례대로 거슬러 줄 수 있을 만큼 거슬러 주면 됩니다
# •
# N 1 260 일 때의 예시를 확인해 봅시다

n = 1260
count = 0
#큰 단위의 화폐부터 차례대로 확인하기
array = [500, 100, 50, 10]
for coin in array:
    count += n // coin
    n %= coin
# 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
print(count)