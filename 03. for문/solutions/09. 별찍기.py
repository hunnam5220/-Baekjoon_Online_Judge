from sys import stdin
ipt = stdin.readline

num = int(ipt().rstrip())

for x in range(1, num+1):
    print('*'*x)

