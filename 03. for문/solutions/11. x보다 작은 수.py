from sys import stdin
ipt = stdin.readline

N, X = ipt().rstrip().split()

num = list(map(int, input().split()))

for step in num:
    if step < int(X):
        print(step, end=' ')
