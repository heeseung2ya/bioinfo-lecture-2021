fr = open('/Users/hanheeseung/Desktop/python/bioinfo-lecture-2021/210708-210709/sequence.nucleotide.gb', 'r')
title = ''

def result():
    for idx, value in enumerate(title.split('TITLE')):
        if idx == 1:
            print(f'  TITLE{value}')
        else:
            print(f'       {value}')


def title_parsing(line):
    global title
    if 'JOURNAL' in line:
        main(line)
    else:
        title += line
        line = fr.readline().strip() + ' '
        title_parsing(line)

def main(line):
    if 'TITLE' in line:
        title_parsing(line)
    elif 'COMMENT' in line:
        result()
        fr.close()
        exit()
    else:
        line = fr.readline().strip() + ' '
        main(line)

if __name__ == '__main__':
    line = fr.readline().strip() + ' '
    main(line)
