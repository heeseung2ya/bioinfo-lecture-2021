def menu():
    print('Option-1) Read a FASTA format DNA sequence file and make a reverse sequence file.')
    print('Option-2) Read a FASTA format DNA sequence file and make a reverse complement sequence file.')
    print('Option-3) Convert GenBank format to FASTA format file.')
    op = input('Select the option: ')
    return op


def op1(fr, fw):
    title = fr.readline().strip()
    seq = ''
    for line in fr:
        seq += line.strip()

    rev = seq[::-1]
    fw.write(title)
    for i in range(0, len(rev), 70):
        fw.write('\n' + rev[i:i+70])

    
def op2(fr, fw):
    title = fr.readline()
    seq = ''
    for line in fr:
        seq += line.strip()
    
    rev = seq[::-1]
    d_complement = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    fw.write(title)
    cnt = 0
    for i in rev:
        cnt += 1
        fw.write(d_complement[i])
        if cnt % 70 == 0: fw.write('\n')


def op3(fr, fw):
    title = '>' + fr.readline().strip()
    while 1:
        if fr.readline().strip().startswith('ORIGIN'): break
    seq = ''
    for line in fr:
        seq += ''.join(line.strip().split()[1:])
    
    fw.write(title)
    cnt = 0
    for i in range(0, len(seq), 70):
        cnt += 1
        fw.write('\n' + seq[i:i+70])


def main():
    # fr = open(input('Enter input file: '), 'r')
    # fw = open(input('Enter output file: '), 'w')
    fr = open('sequence.nucleotide.gb', 'r')
    fw = open('new.sequence.nucleotide.fasta', 'w')
    op = menu()
    if op == '1': op1(fr, fw)
    elif op == '2': op2(fr, fw)
    elif op == '3': op3(fr, fw)
    else: exit()

    fr.close()
    fw.close()


if __name__ == "__main__":
    main()
