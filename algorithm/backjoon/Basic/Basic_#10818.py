#https://www.acmicpc.net/problem/10818
a= int(input())
b= list(map(int,input().split()))

min=b[0]
max=b[0]
for i in range(len(b)):
    if min>b[i]:
        min=b[i]
    if max<b[i]:
        max=b[i]

print(min,max)