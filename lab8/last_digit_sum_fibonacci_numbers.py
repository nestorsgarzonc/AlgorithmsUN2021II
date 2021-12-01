# Uses python3
import sys


def fibonacci_sum_naive(n):
    if n <= 1:
        return n
    previous = 0
    current = 1
    _sum = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current
    return _sum % 10


def get_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    fib = [x for x in range(n+1)]
    fib[0] = 0
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1]+fib[i-2]
    return fib[n]


def fibonacci_huge(n, m):
    index = -1
    for i in range(2, 10**14):
        if(get_fibonacci(i) % m == 0 and get_fibonacci(i+1) % m == 1):
            index = i
            break
    mod_small = n % index
    fib_small = get_fibonacci(mod_small)-1
    return fib_small % m


x = int(input())
print(fibonacci_huge(x+2, 10))
