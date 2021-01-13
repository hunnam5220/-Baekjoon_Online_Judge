from sys import stdin

ipt = stdin.readline

x, y, w, h = ipt().split()
x, y, w, h = int(x), int(y), int(w), int(h)

# w,h 와 (0, 0)이 이루고 있는 사각형 안의 점(x, y)를 기준으로 축까지의 거리를 계산해야 옳다.

print(min([abs(h-y), abs(w-x), y, x]))