def solution(L, x):
    for i in range(len(L)):
        if x in L:
            break
        if L[i] > x:
            L.insert(i,x)
            break
        if L[i] == L[-1]:
            L.append(x)
    return L