title = ""
seq = ""
with open("sequence.protein.2.fasta", "r") as fr:
    for line in fr.readlines():
        if line.startswith(">"):
            title += line.strip()
        else:
            seq += line.strip()
print(f"title: {title}")
print(f"seq: {seq}")
