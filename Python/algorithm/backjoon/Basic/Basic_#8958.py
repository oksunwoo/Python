#https://www.acmicpc.net/problem/8958

n= int(input())

for i in range(n):
   li=input()
   list(li)

   score = 0
   count = 0

   for j in range(len(li)):
      if(li[j]=='O'):
         score+=1
         if(count==0):
            count+=1
         elif(count!=0):
            score=score+count
            count+=1
      else:
         count=0

   print(score)