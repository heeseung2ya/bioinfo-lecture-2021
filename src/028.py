seq = "ATGTTATAG"

# 강사님 코드
comp_data = {"A":"T", "T":"A", "C":"G", "G":"C"}
comp_seq = ""
for s in seq:
    comp_seq += comp_data[s]
print(seq)
print(comp_seq)



# 내 코드
'''
result = ''

for i in s:
    if i == "A":
        result += "T"
    elif i == "T":
        result += "A"
    elif i == "C":
        result += "G"
    elif i == "G":
        result += "C"
print(result)
'''
