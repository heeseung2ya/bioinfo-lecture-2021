TITLE_line = ""
TITLE_idx = 0
blank_idx = 0
file = open("sequence.nucleotide.gb", "r").readlines()
for line in file:
    if len(line.strip().split()) > 0:
        if TITLE_idx == 1 and line.startswith("            "):
            TITLE_line += " " + " ".join(line.strip().split()[:])
            blank_idx = 1
        if line.strip().split()[0] == "TITLE":
            TITLE_idx = 1
            TITLE_line += " ".join(line.strip().split()[1:])
        elif blank_idx == 1 and line.strip().split()[0] != "TITLE":
            TITLE_idx = 0
            blank_idx = 0
            TITLE_line += "\n"

split_TITLE_line = TITLE_line.split("\n")

for line in split_TITLE_line:
    if line == split_TITLE_line[0]:
        TITLE_line = "  TITLE     " + line + "\n"
    else:
        TITLE_line += "            " + line + "\n"

print(TITLE_line)

open("sequence.nucleotide.gb", "r").close()

"""
# 수정 전 코드
first_TITLE_idx = 0


with open("sequence.nucleotide.gb", "r") as fi:
    for line in fi.readlines():
        if line.strip().startswith("TITLE"):
            if first_TITLE_idx == 0:
                print(line.strip())
                first_TITLE_idx = 1
            else:
                print(line.strip().replace("TITLE", "     "))
"""

"""
# 경섭오빠 코드

file_name = "sequence.nucleotide.gb"
ti = ""
cnt = 1
seq_li = list()
with open(file_name, "r") as handle:
    for line in handle:
        line = line.strip()
        if line.startswith("JOURNAL"):
            ti += "\n"
            cnt = 1
        if line.startswith("TITLE"):
            cnt = 2
        if cnt == 2:
            # print (line, end ='')
            ti += line

ti_s = ti.split("\n")


for i in range(len(ti_s)):
    if i == 0:
        print(ti_s[i])
        pass
    if i >= 1:
        print(ti_s[i].replace("TITLE", "     "))
"""
