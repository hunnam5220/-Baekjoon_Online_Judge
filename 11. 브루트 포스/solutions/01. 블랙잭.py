from sys import stdin

ipt = stdin.readline


def solve():
    n, m = ipt().split()

    card_list = list(map(int, ipt().split()))
    card_list = sorted(card_list, reverse=True)
    sum_card_num = 0
    sub_num = 99999999
    result = 0

    for x in range(len(card_list)):
        std = card_list[x]
        for y in range(x + 1, len(card_list)):
            std2 = card_list[y]
            for z in range(y + 1, len(card_list)):
                std3 = card_list[z]
                sum_card_num = std + std2 + std3
                if sum_card_num > int(m):
                    continue
                else:
                    if sum_card_num == int(m):
                        return sum_card_num

                    elif abs(int(m) - sum_card_num) < sub_num:
                        sub_num = abs(int(m) - sum_card_num)
                        result = sum_card_num
    return result


print(solve())
