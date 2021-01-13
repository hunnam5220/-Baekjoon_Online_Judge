from sys import stdin
from math import sqrt

ipt = stdin.readline

num = int(ipt().rstrip())

for step in range(num):
    x1, y1, r1, x2, y2, r2 = ipt().split()
    x1, y1, r1, x2, y2, r2 = int(x1), int(y1), int(r1), int(x2), int(y2), int(r2)

    a = (x1-x2) ** 2
    b = (y1-y2) ** 2

    atob = sqrt(a+b)

    # 교점이 무한대
    ## 좌표간의 거리가 0
    ## and
    ## 각 좌표에서의 거리가 같은 경우
    if atob == 0 and r1 == r2:
        print(-1)

    # 교점이 하나
    ## 외접과 내접
    ### 1. 좌표간의 거리와 각 좌표에서의 거리들의 합의 절댓값이 같은 경우
    ### or
    ### 2. 좌표간의 거리와 각 좌표에서의 거리들의 차의 절댓값이 같은 경우
    elif atob == abs(r1+r2) or atob == abs(r1-r2):
        print(1)

    # 교점이 두개
    ## 1. 각 좌표에서의 거리들의 차의 절댓값이 좌표간의 거리보다 작다
    ## and
    ## 2. 좌표간의 거리가 각 좌표에서의 거리들의 합의 절댓값보다 작다
    elif abs(r1-r2) < atob < abs(r1+r2):
        print(2)

    # 그 외
    else:
        print(0)