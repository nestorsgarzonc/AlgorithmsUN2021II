# Uses python3
import sys


def fibonacci_sum_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1
    _sum = 1

    for i in range(n-1):
        tmp_previous = previous
        previous = current % 10
        current = (tmp_previous + current) % 10
        _sum = (_sum + current) % 10
    return _sum


if __name__ == '__main__':
    _input = input()  # sys.stdin.read()
    n = int(_input)
    print(fibonacci_sum_naive(n % 60, 10))
