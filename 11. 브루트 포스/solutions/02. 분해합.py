from sys import stdin

n = stdin.readline().rstrip()

# for n in range(1, 100001):
#     n = str(n)

check_start = int(n) - 54

if check_start < 0:
    check_start = 10

while True:
    chk_sum_num = check_start + sum(list(map(int, str(check_start))))
    if check_start >= int(n):
        print(0)
        break
    else:
        if chk_sum_num > int(n):
            check_start += 1
            continue
        elif chk_sum_num == int(n):
            print(check_start)
            break
        else:
            check_start += 1