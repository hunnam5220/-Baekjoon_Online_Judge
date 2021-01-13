from sys import stdin

ipt = stdin.readline

step = ipt().rstrip()

print(sum(list(map(int, ipt().rstrip()))))