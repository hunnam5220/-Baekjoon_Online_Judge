from sys import stdin

ipt = stdin.readline

num = int(ipt().rstrip())

arr = sorted(list(map(int, ipt().rstrip().split())))

max_score = arr[-1]

for step in range(len(arr)):
    arr[step] = arr[step]/max_score*100

print(sum(arr)/num)