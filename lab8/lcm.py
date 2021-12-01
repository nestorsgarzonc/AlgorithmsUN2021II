# Uses python3
import sys


def lcm_naive(a: int, b: int) -> int:
    temp: int = 0
    for i in range(1, (a * b)+1):
        temp = a*i
        if (temp % b == 0):
            return temp
    return a * b


if __name__ == '__main__':
    _input = sys.stdin.read()
    a, b = map(int, _input.split())
    print(lcm_naive(a, b))
