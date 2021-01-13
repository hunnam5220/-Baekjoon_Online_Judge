from sys import stdin

ipt = stdin.readline

num = int(ipt().rstrip())

for step in range(num):
    arr_str_ox = list(ipt().rstrip())
    cnt = 1
    for x in range(len(arr_str_ox)):
        if arr_str_ox[x] == 'O':
            arr_str_ox[x] = cnt
            cnt += 1
        else:
            arr_str_ox[x] = 0
            cnt = 1
    print(sum(arr_str_ox))

