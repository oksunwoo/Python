def solution(mylist):
    answer = [[0 for j in range(len(mylist))] for i in range(len(mylist[0]))]

    for i in range(len(mylist)):
        for j in range(len(mylist[i])):
            answer[i][j]=mylist[j][i]

    return answer


mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
solution(mylist)
