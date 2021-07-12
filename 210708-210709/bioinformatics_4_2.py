# with open 쓰지말고 깔끔하게 다시 짜보기

ORIGIN_idx = 0
seq = ""

file = open("sequence.protein.gb", "r").readlines()
for line in file:
    if line.strip() == file[0].strip():
        title = line.strip()
    if ORIGIN_idx == 1:
        seq += "".join(line.strip().split()[1:])
    elif line.strip() == "ORIGIN":
        ORIGIN_idx = 1
open("sequence.protein.gb", "r").close()

print(f"title: {title}")
print(f"seq: {seq}")


"""
# 수정 전 코드
title = ""
seq = ""
idx = 0
cnt = 0
tmp2 = []

with open("sequence.protein.gb", "r") as fr:
    for line in fr.readlines():
        if cnt == 0:
            title = line.strip()
        tmp = line.strip()
        if tmp.startswith("ORIGIN"):
            idx = 1
        elif idx == 1:
            tmp2.append("".join(line.strip().split()[1:]))
            seq = "".join(tmp2).strip()
        cnt += 1
print(f"title: {title}")
print(f"seq: {seq}")
"""
