fr = open('sequence.protein.gb', 'r')

title = fr.readline().strip()
while 1:
    if fr.readline().strip().startswith('ORIGIN'): break

seq = ''
for line in fr:
    seq += ''.join(line.lstrip().split()[1:])

for i in range(0, len(seq), 70):
    print(seq[i:i+70])
