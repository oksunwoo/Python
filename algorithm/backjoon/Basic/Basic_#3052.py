#https://www.acmicpc.net/problem/3052
a=[]
for i in range(10):
   a.append(int(input()))
   #a[i]=int(input())
   a[i]=a[i]%42
b=set()
for i in range(len(a)):
   b.add(a[i])

print(len(b))