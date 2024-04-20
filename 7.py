for S in range(1, 9 + 1):
    for E in range(0, 9 + 1):
        for N in range(0, 9 + 1):
            for D in range(0, 9 + 1):
                for M in range(1, 9 + 1):
                    for O in range(0, 9 + 1):
                        for R in range(0, 9 + 1):
                            x_1 = int(str(S) + str(E) + str(N) + str(D))
                            x_2 = int(str(M) + str(O) + str(R) + str(E))
                            y = str(x_1 + x_2)
                            if len(y) == 5 and y[-4] == str(O) and y[-3] == str(N) and y[-2] == str(E):
                                if y[-5] == str(M) and y[-1] != str(S) and y[-1] != str(E) and y[-1] != str(N):
                                    if y[-1] != str(D) and y[-1] != str(M) and y[-1] != str(O) and y[-1] != str(R):
                                        print(x_1, x_2, y)
