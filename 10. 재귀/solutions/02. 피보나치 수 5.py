from sys import stdin

def fibonacci_num(n, arr):
    if n > 0:
        arr.append(sum(arr[-2:]))
        return fibonacci_num(n-1, arr)
    else:
        return arr

arr = [0, 1]
n = int(stdin.readline().rstrip())
result = fibonacci_num(n, arr)

print(result[n])