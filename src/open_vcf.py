cnt = 0
pass_cnt = 0


with open("070.vcf", "r") as handle:
    for line in handle:
        if line.startswith("##"):
            continue
        elif line.startswith("#") == False:
            cnt += 1

            if line.strip().split("\t")[6] == "PASS":
                pass_cnt += 1

print(f"data 행 갯수: {cnt}")
print(f"PASS 갯수: {pass_cnt}")
