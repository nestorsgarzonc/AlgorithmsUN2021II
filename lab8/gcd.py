# Uses python3
import sys


def gcd_naive(a: int, b: int) -> int:
    a1: int = a % b
    if (a1 == 0):
        return b
    else:
        return gcd_naive(b, a1)


if __name__ == "__main__":
    _input = sys.stdin.read()
    a, b = map(int, _input.split())
    print(gcd_naive(a, b))
