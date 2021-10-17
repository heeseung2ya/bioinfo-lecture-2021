fr = open('sequence.protein.2.fasta', 'r')

title = fr.readline().strip()
seq = ''
for line in fr:
    seq += line.strip()

aa = ''
while aa != 'XXX':
    aa = input('Searching for: ')
    print('Found at:', ', '.join(map(str, [idx + 1 for idx, value in enumerate(seq) if value == aa])))
print('Okay, I will stop.')
