N,M,K = map(int,input().split())
data = list(map(int,input().split()))
data.sort()

count = 0
answer = 0

for i in range(M):
    if count < K:
        answer += data[-1]
        count += 1
    else:
        answer += data[-2]
        count = 0

print(answer)