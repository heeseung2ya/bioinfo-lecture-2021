title = ""
seq = ""
idx = 0
cnt = 0

with open("sequence.protein.gp", "r") as fr:
    for line in fr.readlines():
        tmp = line.strip()
        if cnt == 0:
            title = line.strip()
        if tmp.startswith("ORIGIN"):
            idx = 1
        elif idx == 1:
            seq += line
        cnt += 1
print(f"title: {title}")
print(f"seq: {seq}")
