with open("sequence.protein.fasta", "r") as fr:
    for line in fr.readlines():
        if line.startswith(">"):
            print(line.strip())
        else:
            print(line.strip(), end="")
