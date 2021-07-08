s1 = input("Enter s1: ")
s2 = input("Enter s2: ")

if len(s1) % 2 == 1 and len(s1) < len(s2):
    print(f"{s1}{s2}")
else:
    print(f"{s2}{s1}")
