from sys import stdin

ipt = stdin.readline

a_b_v = list(map(int, ipt().split()))

a, b, v = a_b_v[0], a_b_v[1], a_b_v[2]

days = 0

if (v-b) % (a-b) == 0:
    print((v-b) // (a-b))
else:
    print((v-b) // (a-b) + 1)