def solution(lottos, win_nums):
    answer = []
    count=0
    z_count=0
    rank = 7

    for i in range(len(lottos)):
        for j in range(len(win_nums)):
            if lottos[i] == win_nums[j]:
                count += 1
        if lottos[i] == 0:
            z_count += 1

    max = rank-(count+z_count)
    min = rank-count

    if max==7:
        max=6
    if min ==7:
        min=6
    answer.append(max)
    answer.append(min)

    return answer