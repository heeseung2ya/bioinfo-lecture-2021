import sys


try:
    with open('noname.txt', 'r') as fr:
        read = fr.readlines()
except FileNotFoundError as err:
    print(f'{err}')
    #sys.exit(1)
    #또는, 파일이 없으면 해당 파일을 만드는 처리도 가능. (해보자!)

print(read)
