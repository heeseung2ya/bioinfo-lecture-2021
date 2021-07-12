input_name = input("Enter input file: ")
output_name = input("Enter output file: ")
print(
    "\n\
Option-1) Read a FASTA format DNA sequence file and make a reverse sequence file.\n\
Option-2) Read a FASTA format DNA sequence file and make a reverse complement sequence file.\n\
Option-3) Convert GenBank format file to FASTA format file."
)

select = int(input("Select the option: "))

seq = ""
fasta_file = open(input_name, "r").readlines()
for line in fasta_file:
    if line.startswith(">"):
        header = line
    else:
        seq += line.strip()
open(input_name, "r").close()

rev_seq = seq[::-1]
if select == 1:
    with open(output_name, "w") as file:
        file.write(header)
        file.write(rev_seq)
elif select == 2:
    d_rev_com = {"A": "T", "C": "G", "G": "C", "T": "A"}
    rev_com_seq = ""
    for base in rev_seq:
        rev_com_seq += d_rev_com[base]
    with open(output_name, "w") as file:
        file.write(header)
        file.write(rev_com_seq)
elif select == 3:
    GBtoFASTA_header = ">"
    GBtoFASTA_seq = ""

    file = open(input_name, "r").readlines()
    ORIGIN_idx = 0
    for line in file:
        if line.strip() == file[0].strip():
            GBtoFASTA_header += line.strip() + "\n"
        if ORIGIN_idx == 1:
            GBtoFASTA_seq += "".join(line.strip().split()[1:])
        elif line.strip() == "ORIGIN":
            ORIGIN_idx = 1
    open(input_name, "r").close()

    with open(output_name, "w") as file:
        file.write(GBtoFASTA_header)
        file.write(GBtoFASTA_seq)
