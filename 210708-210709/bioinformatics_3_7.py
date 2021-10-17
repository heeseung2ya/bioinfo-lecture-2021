fr = open('sequence.protein.2.fasta', 'r')

title = fr.readline().strip()
seq = ''
for line in fr:
    seq += line.strip()

pos = ''
while 1:
    pos = input('Position: ')
    if pos == 'XXX':
        print('Okay, I will stop.')
        break
    else:
        pos = int(pos)
        print('Three amino acids:', seq[pos - 1 : pos - 1 + 3])
