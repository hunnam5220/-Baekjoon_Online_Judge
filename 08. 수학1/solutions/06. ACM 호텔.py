from sys import stdin

ipt = stdin.readline

step = int(ipt().rstrip())

for x in range(step):
    result = ''
    arr = list(map(int, ipt().split()))
    h, w, n = arr[0], arr[1], arr[2]

    if n % h == 0:
        yy = str(h)
        xx = str(n // h)
    else:
        yy = str(n % h)
        xx = str(n // h + 1)

    if len(xx) == 1:
        xx = '0'+xx
        result += yy+xx
    else:
        result += yy + xx

    print(int(result))