from sys import stdin
ipt = stdin.readline

a, b = ipt().rstrip().split()

print(max(int(''.join(list(reversed(a)))), int(''.join(list(reversed(b))))))