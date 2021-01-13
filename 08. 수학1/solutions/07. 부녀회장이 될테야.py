from sys import stdin

ipt = stdin.readline

step = int(ipt().rstrip())
floor = []

for x in range(step):
    k, n = int(ipt().rstrip()), int(ipt().rstrip())

    arr = [x for x in range(1, n+1)]
    cnt = k

    for z in range(k):
        if cnt == 0:
            print(sum(arr))
        else:
            cnt -= 1
            for y in range(1, n+1):
                floor.append(sum(arr[:y]))
            arr = floor
            floor = []

    print(arr[n - 1])