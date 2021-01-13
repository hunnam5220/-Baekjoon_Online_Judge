from sys import stdin

ipt = stdin.readline
num = ipt().rstrip()

num_arr = sorted(list(map(int, ipt().split())))
print('{} {}'.format(num_arr[0], num_arr[-1]))