N, d, R = map(int, input().split())
D = 2 * d + 2 * R
L = N * D - 2 * d * (N - 1)
print(L)
