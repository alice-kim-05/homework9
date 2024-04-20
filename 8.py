x = int(input())
k = 0
for i in range(1, x + 1):
    for n in range(1, x + 1):
        if ((i ** 2) + (n ** 2)) == x:
            k += 1
            print(i, n)
print(round(k / 2))
