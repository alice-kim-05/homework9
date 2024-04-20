N = int(input())
k = 0
for i in range(0, N + 1):
    for n in range(N, i-1, -1):
        k += i
        k += n
print(k)
