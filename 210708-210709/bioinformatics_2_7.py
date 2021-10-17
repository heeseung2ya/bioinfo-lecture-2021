d_codon = {}

def build():    
    global d_codon
    codon = ""
    while codon != 'XXX':
        codon = input('Enter three-base codon to build: ')
        aa = input('Enter amino acid: ')
        d_codon[codon] = aa
    print('Okay, I will switch.')

def search():
    global d_codon
    codon = ""
    while codon != 'XXX':
        codon = input('Enter three-base codon to search: ')
        print(f'Amino acid for {codon}: {d_codon[codon]}')
    print('Okay, I will stop.')

def main():
    build()
    search()


if __name__ == "__main__":
    main()
