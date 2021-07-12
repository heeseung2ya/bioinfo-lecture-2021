firstline_idx = 0
seq = ""
with open("sequence.nucleotide.fasta", "r") as fi:
    for line in fi.readlines():
        if line.startswith(">"):
            firstline_idx = 1
            header = line.strip()
        else:
            seq += line.strip()

for i in range(0, len(seq), 3):
    if len(seq[i:]) > 3:
        print(seq[i : i + 3])
    else:
        print(seq[i:])
