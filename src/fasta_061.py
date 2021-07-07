data = '061.fastq'

cnt = 0
line_num = 0

with open('061.fastq', 'r') as db:
    for line in db:
        if line_num % 4 == 0:
            pass
        elif line_num % 4 == 1:
            for base in linde.strip():
                if base not in data:
                    data[base] = 0
                eata[base] += 1
        elif line_num % 4 == 2:
            pass
        elif line_num % 4 == 3:
            pass
        cnt += 1
        

print(cnt / 4)
print(data)
