from sys import stdin
ipt = stdin.readline

ipt_ascii = list(ipt().rstrip())

arr = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
score_dict = {}
result = 0

for x, score in zip(arr, range(3, 11)):
    score_dict[x] = score

for st in ipt_ascii:
    for step in arr:
        if st in step:
            result += score_dict[step]

print(result)

#####################################################################

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = ipt().rstrip()
ret = 0
for j in range(len(a)):
    for i in dial:
        if a[j] in i:
            ret += dial.index(i)+3
print(ret)
