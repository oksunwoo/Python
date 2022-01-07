# print('\"C:\\Download\\\'hello\'.py\"')
#
#
# print("print(\"Hello\\nWorld\")")
#

# a,b = input().split(':')
# print(a, b, sep=':')
#
# print(a,b)
# print(a,"",b)
# print(a+b)

#
# c,d =map(float,input().split())
# print(c+d)
#
# a=int(input())
# print('%o'%a)
#
# c=ord(input())
# print(chr(c+1))

# a,b=map(float,input().split())
# print(format(a/b,'.3f'))

# a= 1
# b= 5
# c= 10
# #
# # print(a==b)
#
# print((b if a>b else a) if c>b else (c if a>c else a))
#


# while True:
#     n=int(input())
#     if n == 0:
#       break
#     print(n)


# n = int(input())
#
# for i in range(n-1,-1,-1):
#     print(i)

# c = ord(input())
#
# for ch in range(ord('a'),c+1,1):
#     print(chr(ch))

# n = int(input())
#
# for i in range(0,n,1):
#     print(i)
#
# n = int(input())
#
# sum = 0
# for i in range(n+1):
#     if i%2 == 0:
#         sum += i
# print(sum)


# while True:
#     c = input()
#     print(c)
#     if 'q' == c:
#         break

# a,b = map(int,input().split())
#
# for i in range(1,a+1,1):
#     for j in range(1,b+1,1):
#         print(i,j)


# hexa = input()
# hexa = int(hexa,16)
# for i in range(1,16):
#     print('%X'%hexa,'*','%X'%i,'=','%X'%(i*hexa),sep="")
#
#

# clap = int(input())
#
# for i in range(1,clap+1):
#     if i%10 == 3 or i%10 ==6 or i%10 == 9 :
#         print("X",end=" ")
#     else:
#         print(i,end=" ")
#
#
#

# r,g,b = map(int,input().split())
#
# count = 0
# for i in range(r):
#     for j in range(g):
#         for k in range(b):
#             count += 1
#             print(i,j,k)
#
# print(count)

# h,b,c,s = map(int,input().split())
#
# result = h*b*c*s/8/1024/1024
#
# print(round(result,1),"MB")

# r,g,b = map(int,input().split())
#
# result = r*g*b/8/1024/1024
#
# print(f'{result:.2f}')

# num = int(input())
#
# sum=0
# i=0
# while sum<num:
#     i+=1
#     sum+=i
# print(sum)


# num = int(input())
#
# for i in range(1,num+1):
#     if i%3==0:
#         continue
#     print(i)
#

# a,d,n = map(int,input().split())
#
# i=1
# while i<n:
#     a += d
#     i += 1
# print(a)

# a,r,n = map(int,input().split())
#
# i=1
# while i<n:
#     a *= r
#     i += 1
# print(a)

# a,m,d,n = map(int,input().split())
#
# i=1
# while i<n:
#     a = a*m + d
#     i += 1
# print(a)

# a,b,c = map(int,input().split())
#
# day = 1
#
# while day%a != 0 or day%b != 0 or day%c != 0:
#     day += 1
# print(day)
#
# a=[]
# for i in range(23):
#     a.append(0)
#
# student = int(input())
# d = list(map(int,input().split()))
#
# for j in range(student):
#     a[d[j]-1] += 1
#
# for k in a:
#     print(k,end=" ")
#

# a = int(input())
# student = list(map(int,input().split()))
#
# for i in range(a-1,-1,-1):
#     print(student[i], end=" ")

# a = int(input())
# b = list(map(int,input().split()))
#
# print(min(b))

# d = [[0 for j in range(19)]for i in range(19)]
#
# a = int(input())
# for i in range(a):
#      b,c = map(int,input().split())
#      if d[b-1][c-1] == 1:
#          continue
#      else:
#          d[b-1][c-1] += 1
# for i in range(19):
#     for j in range(19):
#         print(d[i][j],end=" ")
#     print()

#
# mat=[]
#
# for i in range(19):
#      mat.append((list(map(int,input().split()))))

n = int(input())
a = []
for i in range(n):
    a.append((list(map(int,input().split()))))

for 













