from sys import stdin
ipt = stdin.readline
num = int(ipt())

for x in range(1, 10):
    print("{} * {} = {}".format(num, x, num * x))