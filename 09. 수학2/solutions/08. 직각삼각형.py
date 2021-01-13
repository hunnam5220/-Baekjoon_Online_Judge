from sys import stdin
ipt = stdin.readline

while True:
    num_list = sorted(list(map(int, ipt().split())))
    if num_list[0] == num_list[1] == num_list[2]:
        break
    max_num = num_list[-1] ** 2
    check_num = sum([x**2 for x in num_list[:2]])

    if check_num == max_num:
        print('right')
    else:
        print('wrong')
