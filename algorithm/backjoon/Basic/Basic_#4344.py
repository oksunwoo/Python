#https://www.acmicpc.net/problem/4344
C=int(input())

for i in range(C):
   a=list(map(int, input().split()))
   sum=0
   for j in range(1,len(a)):
      sum+=a[j]
   #print(sum, " sum")
   avg=sum/a[0]
   #print(avg," avg")
   count=0
   for k in range(1,len(a)):
      if(a[k]>avg):
         count+=1
   #print(count," count")
   print(format(count/a[0]*100,".3f")+"%")