from sys import stdin

ipt = stdin.readline

step_num = int(ipt().rstrip())

for step in range(step_num):
    cycle_num, cycle_str = ipt().rstrip().split()
    cycle_str = list(cycle_str)
    print_str = ''
    for char_code in cycle_str:
        for x in range(int(cycle_num)):
            print_str += char_code

    print(print_str)