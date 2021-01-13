from collections import Counter as cc
from sys import stdin

ipt = stdin.readline
input_num = 1

for x in range(3):
    input_num *= int(ipt().rstrip())

result = cc(list(str(input_num)))

for step in range(0, 10):
    try:
        print(result[str(step)])
    except:
        print(0)