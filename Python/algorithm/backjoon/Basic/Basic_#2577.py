#https://www.acmicpc.net/problem/2577
A=int(input())
B=int(input())
C=int(input())

result= A*B*C
p=list(map(int,str(result)))
q=[0,0,0,0,0,0,0,0,0,0]
for i in range(len(p)):
        if p[i] == 0:
            q[0]+=1
        if p[i] == 1:
            q[1]+=1
        if p[i] == 2:
            q[2]+=1
        if p[i] == 3:
            q[3]+=1
        if p[i] == 4:
            q[4]+=1
        if p[i] == 5:
            q[5]+=1
        if p[i] == 6:
            q[6]+=1
        if p[i] == 7:
            q[7]+=1
        if p[i] == 8:
            q[8]+=1
        if p[i] == 9:
            q[9]+=1
for i in range(len(q)):
    print(q[i])