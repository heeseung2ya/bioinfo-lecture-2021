#! /usr/bin/python

import sys

print(sys.argv)


for i in sys.argv[1:]:
    print(f'Hello {i}')
