total = 0

with open("077.bed", "r") as db:
    for line in db.readlines():
        tmp = line.strip().split("\t")
        chr = tmp[0]
        start = int(tmp[1])
        end = int(tmp[2])
        length = end - start
        total += length
print(f"{chr} {total}")
