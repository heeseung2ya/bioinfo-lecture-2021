d_codon = {}
print_codon = ""

while print_codon != "XXX":
    in_codon = input("Enter three-base codon to build: ")
    if in_codon == "XXX":
        print("Okay, I will switch.")
        while True:
            print_codon = input("Enter three-base codon to search: ")
            if print_codon == "XXX":
                print("Okay, I will stop.")
                break
            print(f"Amino acid for {print_codon}: {d_codon[print_codon]}")
    else:
        in_aa = input("Enter amino acid: ")
        d_codon[in_codon] = in_aa


def build_codon():
    pass


def search_codon():
    pass
