def solution(x):
    return recursive(x)


def recursive(n):
    if n >= 2:
        return recursive(n-1)+recursive(n-2)
    else:
        return n

print(solution(10))