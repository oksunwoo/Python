N = int(input())

pen = list(map(str,input()))
pen.append('T')

count = [1] * 2

for i in range(N):
    if pen[i] == 'B':
        continue
    elif pen[i] == 'R':
        count[0] += 1
        if pen[i+1] == 'R':
            count[0] -= 1


for i in range(N):
    if pen[i] == 'R':
        continue
    elif pen[i] == 'B':
        count[1] += 1
        if pen[i+1] =='B':
            count[1] -= 1

print(min(count))