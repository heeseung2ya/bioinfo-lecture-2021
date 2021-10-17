fr = open('sequence.protein.fasta', 'r')
fw = open('sequence.protein.2.fasta', 'w')

for line in fr:
    fw.write(line)
