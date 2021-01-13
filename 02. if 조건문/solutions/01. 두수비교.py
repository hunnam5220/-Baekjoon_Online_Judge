import sys
ipt = sys.stdin.readline
a, b = ipt().split()

if int(a) > int(b):
    print('>')
elif int(a) < int(b):
    print('<')
else:
    print('==')
