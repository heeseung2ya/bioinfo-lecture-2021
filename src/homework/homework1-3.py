# 염기 한 글자를 받아 fullname을 출력하는 프로그램

import sys


def get_base(base):
    d_base = {
        "A": "Adenine",
        "C": "Cytosine",
        "G": "Guanine",
        "T": "Thymine",
        "U": "Uracil",
    }

    print(f"{base} {d_base[base]}")


get_base(sys.argv[1])
