n = int(input())

main_lst = []

for i in range(n):
    lst = [1] * (i+1)
    for j in range(i+1):
        if j != 0 and j != i:
            lst[j] = main_lst[i-1][j-1] + main_lst[i-1][j]
    main_lst.append(lst)

for k in main_lst:
    print(k)

