def re(i):
    if i == 100 :
        return
    print(i, '번째 재귀함수를 출력한다')
    re(i+1)
re(1)