n = int(input())

x, y = 1, 1
plans = input().split()


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move_types = ['L', 'R', 'U', 'D']

for plan in plans :
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            # 이동하려는 것이 어떤 타입인지를 move_types를 돌면서 확인 
    
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue # 씹고 다음 것으로 넘어감 
    x, y = nx, ny


print(x, y)