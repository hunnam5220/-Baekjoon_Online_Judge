from sys import stdin
from math import sqrt as sq

ipt = stdin.readline
step = int(ipt().rstrip())
arr = list(map(int, ipt().split()))
cnt = 0

for x in range(step):
    tmp = True
    if arr[x] - 1 > 0:
        for y in range(2, int(sq(arr[x]))+1):
            if arr[x] % y == 0:
                tmp = False
                break
        if tmp is False:
            continue
        else:
            # print(arr[x])
            cnt+=1
    else:
        continue

print(cnt)