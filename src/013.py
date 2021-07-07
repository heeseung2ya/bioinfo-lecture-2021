import sys

if len(sys.argv) < 2:
    print(f"#usage: python  {sys.argv[0]} [num]")
    sys.exit()

for i in sys.argv[1:]:
    print(f"Hello {i}")
