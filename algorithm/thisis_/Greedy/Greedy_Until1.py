n,k = map(int,input().split())


count = 0


while n != 1:
    if n/k == n//k:
        n = n/k
    else:
        n -= 1
    count += 1


print(count)
