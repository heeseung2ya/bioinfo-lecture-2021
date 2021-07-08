with open("sequence.protein.2.fasta", "r") as fr:
    print("The second line is: ", end="")
    for line in fr.readlines():
        if line.startswith(">"):
            continue
        else:
            print(line, end="")
