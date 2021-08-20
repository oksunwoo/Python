N = int(input())

atm = list(map(int,input().split()))

atm.sort()

waiting = 0
result = 0
for i in range(N):
    waiting += atm[i]
    result += waiting

print(result)