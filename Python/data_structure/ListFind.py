def solution(L, x):
    answer = []
    if x in L:
        for i in range(len(L)):
            if x == L[i]:
                answer.append(i)
    else:
        answer.append(-1)

    return answer