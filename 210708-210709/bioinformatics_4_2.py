title = ""
seq = ""
idx = 0
cnt = 0
tmp2 = []

with open("sequence.protein.gp", "r") as fr:
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
