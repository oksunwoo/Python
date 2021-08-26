n, k = map(int, input().split())

coin = []

for i in range(n):
    i = int(input())
    coin.append(i)

coin.sort(reverse=True)

count = 0
for item in coin:
    if item > k:
        continue
    else:
        count += k//item
        k %= item

print(count)