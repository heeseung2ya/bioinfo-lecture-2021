tmp = ""
with open("sequence.protein.fasta", "r") as fr:
    for line in fr.readlines():
        tmp += line.strip()
        if line.startswith(">"):
            tmp += "\n"

with open("sequence.protein.2.fasta", "w") as fr:
    fr.write(tmp.strip())
