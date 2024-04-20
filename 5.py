for i in range(0, 999_999 + 1):
    st = '0' * 5 + str(i)
    if st[-1] == st[-5] and st[-2] == st[-4]:
        i += 1
        st_1 = '0' * 5 + str(i)
        if st_1[-1] == st_1[-5] and st_1[-2] == st_1[-4]:
            i += 1
            st_2 = '0' * 5 + str(i)
            if st_2[-2] == st_2[-5] and st_2[-3] == st_2[-4]:
                i += 1
                st_3 = '0' * 5 + str(i)
                if st_3[-3:] == st_3[-4:-7:-1]:
                    print(i-3)
