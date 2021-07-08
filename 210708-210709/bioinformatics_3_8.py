title = ""
seq = ""
result = []

with open("sequence.protein.2.fasta", "r") as fr:
    for line in fr.readlines():
        if line.startswith(">"):
            title += line.strip()
        else:
            seq += line.strip()

while True:
    search = input("Searching for: ")
    if search == "XXX":
        print("Okay, I will stop.")
        break
    else:
        print("Found at: ", end="")
        for i in range(len(seq)):
            if search == seq[i]:
                result.append(str(i + 1))
        print(", ".join(result))
