N,M = map(int,input().split())

data = []
for i in range(N):
    num = list(map(int,input().split()))
    data.append(min(num))
print(max(data))