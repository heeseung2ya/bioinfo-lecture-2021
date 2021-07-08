title = ""
seq = ""

with open("sequence.protein.2.fasta", "r") as fr:
    for line in fr.readlines():
        if line.startswith(">"):
            title += line.strip()
        else:
            seq += line.strip()

while True:
    pos = input("Position: ")
    if pos == "XXX":
        print("Okay, I will stop.")
        break
    else:
        int_pos = int(pos)
        print(f"Three amino acids: {seq[int_pos - 1 : int_pos - 1 + 3]}")
