first_TITLE_idx = 0
with open("sequence.nucleotide.gb", "r") as fi:
    for line in fi.readlines():
        if line.strip().startswith("TITLE"):
            if first_TITLE_idx == 0:
                print(line.strip())
                first_TITLE_idx = 1
            else:
                print(line.strip().replace("TITLE", "     "))
