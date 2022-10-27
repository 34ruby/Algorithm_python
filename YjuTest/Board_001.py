data = input()
# print(data[0])
# print(data[1])
row = int(data[1])
col = ord(data[0]) - ord('a') + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
result = 0

# 나이트가 이동할 수 있는 8가지 방향 각각에 대해서 현재 좌표를 기준으로 움직였을 때 정원 안인 경우의 수를 계산
for step in steps :
    # print(step)
    # print(step[0], ', ', step[1])
    next_row = row + step[0]
    next_col = col + step[1]
    # 정원 안이면 result를 1증가 시키자
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8 :
        result += 1

print(result)