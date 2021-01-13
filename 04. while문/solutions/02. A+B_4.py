from sys import stdin
ipt = stdin.readline
while True:
    try:
        a, b = map(int, ipt().rstrip().split())
        print(a+b)
    except:
        break