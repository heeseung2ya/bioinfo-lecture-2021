# 미완성 코드!!!!

"""
d_codon = {
    "TTT": "F",
    "TTC": "F",
    "TTA": "L",
    "TTG": "L",
    "TCT": "S",
    "TCC": "S",
    "TCA": "S",
    "TCG": "S",
    "TAT": "Y",
    "TAC": "Y",
    "TAA": "*",
    "TAG": "*",
    "TGT": "C",
    "TGC": "C",
    "TGA": "*",
    "TGG": "W",
    "CTT": "L",
    "CTC": "L",
    "CTA": "L",
    "CTG": "L",
    "CCT": "P",
    "CCC": "P",
    "CCA": "P",
    "CCG": "P",
    "CAT": "H",
    "CAC": "H",
    "CAA": "Q",
    "CAG": "Q",
    "CGT": "R",
    "CGC": "R",
    "CGA": "R",
    "CGG": "R",
    "ATT": "I",
    "ATC": "I",
    "ATA": "I",
    "ATG": "M",
    "ACT": "T",
    "ACC": "T",
    "ACA": "T",
    "ACG": "T",
    "AAT": "N",
    "AAC": "N",
    "AAA": "K",
    "AAG": "K",
    "AGT": "S",
    "AGC": "S",
    "AGA": "R",
    "AGG": "R",
    "GTT": "V",
    "GTC": "V",
    "GTA": "V",
    "GTG": "V",
    "GCT": "A",
    "GCC": "A",
    "GCA": "A",
    "GCG": "A",
    "GAT": "D",
    "GAC": "D",
    "GAA": "E",
    "GAG": "E",
    "GGT": "G",
    "GGC": "G",
    "GGA": "G",
    "GGG": "G",
}

firstline_idx = 0
seq = ""
seq60 = ""
with open("sequence.nucleotide.fasta", "r") as fi:
    for line in fi.readlines():
        if line.startswith(">"):
            firstline_idx = 1
            header = line.strip()
        else:
            seq += line.strip()


line_cnt = 0
aa = ""
for i in range(0, len(seq), 60):
    line_cnt += 1
    if len(seq) > 60:
        seq60 += seq[i : i + 60] + "\n"
    else:
        seq60 += seq[i:]
print(seq)
print(d_codon[seq[0:3]])
codon = ""
for i in range(0, len(seq), 3):
    if (i + 1) % 60 != 0:
        print("1")
        print(d_codon[seq[i : i + 3]] + "  ", end="")
        codon += d_codon[seq[i : i + 3]] + "  "
    else:
        codon += "\n"
print(codon)
"""
