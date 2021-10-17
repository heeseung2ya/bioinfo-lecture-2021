fr = open('sequence.protein.gb', 'r')

title = fr.readline().strip()
while 1:
    if fr.readline().strip().startswith('ORIGIN'): break

seq = ''
for line in fr:
    seq += line.lstrip()

print('title:', title)
print('seq:', seq)
