l_num = [3, 1, 1, 2, 0, 0, 2, 3, 3]
d_num = {}

for i in l_num:
    if i not in d_num:
        d_num[i] = 1
    else:
        d_num[i] += 1
print(d_num)

