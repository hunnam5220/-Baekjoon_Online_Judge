from sys import stdin

ipt = stdin.readline

arr = []

for step in range(10):
    arr.append((int(ipt().rstrip())) % 42)

print(len(list(set(arr))))