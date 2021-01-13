from sys import stdin

ipt = stdin.readline
num = int(ipt().rstrip())
result = 0
x = 2
y = 3

if num == 1:
    print(1)
else:
    while result < num:
        result = x * y + 1
        if result < num:
            x += 1
            y += 3
        else:
            print(x)
            break
