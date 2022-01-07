#https://www.acmicpc.net/problem/10871
a = int(input())
count=0
i=0
new=a
while (1):
    b = new//10
    #print(b,"b")
    c = new%10
    #print(c, "c")
    d = b+c
    #print(d, "d")
    new = c*10 + d%10
    #print(new, "new")
    count+=1
    #print(count,"count")
    if new == a:
        break

print(count)