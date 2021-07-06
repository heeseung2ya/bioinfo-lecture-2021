s = "AGTTTATAG"
for i in range(len(s)):
    if s[i:i+2] == "TT":
        print(i)
