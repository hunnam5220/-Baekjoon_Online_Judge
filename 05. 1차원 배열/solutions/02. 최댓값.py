from sys import stdin

ipt = stdin.readline
arr = []
for num in range(9):
    arr.append(list(map(int, ipt().rstrip().split())))

max_num = max(arr)

for step in range(9):
    if max_num == arr[step]:
        print(max_num[0])
        print(step+1)