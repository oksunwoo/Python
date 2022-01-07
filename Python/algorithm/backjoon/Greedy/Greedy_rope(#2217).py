N = int(input())

rope = []
for i in range(N):
    rope.append(int(input()))

rope.sort(reverse=True)

data = []
for i in range(N):
   data.append(rope[i]*(i+1))

print(max(data))