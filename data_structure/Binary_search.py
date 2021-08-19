def solution(L, x):
    lower = 0
    upper = len(L)-1

    while lower <= upper:
        idx = (lower + upper) // 2
        if L[idx] == x:
            return idx
        elif L[idx] > x:
            upper = idx - 1
        elif L[idx] < x:
            lower = idx + 1
    return -1

L = [1, 2, 3]
x = 3
print(solution(L,x))
