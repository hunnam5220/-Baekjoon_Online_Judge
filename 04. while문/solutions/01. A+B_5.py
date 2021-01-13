from sys import stdin
ipt = stdin.readline
step = True
while step:
    num_list = list(map(int, ipt().rstrip().split()))
    if 0 == num_list[0] and 0 == num_list[1]:
        step = False
    else:
        print(sum(num_list))