# with open 쓰지말고 깔끔하게 다시 짜보기

ORIGIN_idx = 0
seq = ""

file = open("sequence.protein.gb", "r").readlines()
for line in file:
    if line.strip() == file[0].strip():
        title = line.strip()
    if ORIGIN_idx == 1:
        seq += line.lstrip()
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

with open("sequence.protein.gb", "r") as fr:
    for line in fr.readlines():
        tmp = line.strip()
        if cnt == 0:
            title = line.strip()
        if tmp.startswith("ORIGIN"):
            idx = 1
        elif idx == 1:
            seq += line.lstrip()
        cnt += 1
seq = seq.strip()
print(f"title: {title}")
print(f"seq: {seq}")
"""
