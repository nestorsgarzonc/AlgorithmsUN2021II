# Uses python3

def calc_fib(n: int) -> int:
    aux_1: int = 0
    aux_2: int = 1
    if(n == 0):
        return 0
    for _ in range(n-1):
        aux_2 += aux_1
        aux_1 = aux_2 - aux_1
    return aux_2


n = int(input())
print(calc_fib(n))
