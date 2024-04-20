for A in range(1, 9+1):
    for B in range(0, 9 + 1):
        x = int(str(A) + str(B))
        y = str(x * x)
        if y[-1] == str(B) and y[-2] == str(A) and len(y) == 3:
            print(y)