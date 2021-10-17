fr = open('sequence.protein.2.fasta', 'r')

title = fr.readline().strip()
seq = ''
for line in fr:
    seq += line.strip()

print('title:', title)
print('seq:', seq)
