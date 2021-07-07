d_sample = {}
with open("2-4.csv", "r") as FI:
    data = FI.readlines()
    line1 = data[0].strip().split(",")
    line2 = data[1].strip().split(",")

    for i in range(len(line1)):
        d_sample[line1[i]] = float(line2[i])

print(d_sample)
print("".join(d_sample))

# with open("2-4.json", "w") as FI:
#     FI.write(d_sample)

# 음...? 딕셔너리는 어떻게 써야하지 그럼...
# Traceback (most recent call last):
#   File "homework2-4.py", line 13, in <module>
#     FI.write(d_sample)
# TypeError: write() argument must be str, not dict

