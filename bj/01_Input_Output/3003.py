chessDefault = [1, 1, 2, 2, 2, 8]

myPiece = list(map(int, input().split()))

for i in range(6):
    print(chessDefault[i] - myPiece[i])