from sys import stdin

ipt = stdin.readline

str_ipt = ipt().rstrip()

arr = [-1] * 123
cnt = 0

str_ascii = list(map(ord, str_ipt))

for step in str_ascii:
    if arr[step] == -1:
        arr[step] = cnt
    cnt+=1

for step in arr[97:]:
    print(step, end=' ')