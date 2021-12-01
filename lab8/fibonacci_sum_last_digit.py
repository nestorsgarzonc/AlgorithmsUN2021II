# Uses python3
import sys


def fibonacci_partial_sum_naive(from_, to):
    _sum = 0
    current = 0
    _next = 1
    for i in range(to + 1):
        if i >= from_:
            _sum += current
        current, _next = _next, current + _next
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
    fib_small = get_fibonacci(mod_small)
    return fib_small


def fibonacci_partial_sum(from_, to):
    if from_ == to:
        return fibonacci_huge(from_, 10) % 10
    return ((fibonacci_huge(to+2, 10)-1) - (fibonacci_huge(from_+1, 10)-1)) % 10


if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum(from_, to))
