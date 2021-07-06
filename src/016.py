file_name = "read_sample.txt"

# 방법1
with open(file_name, "r") as handle:
    for line in handle:
        print(line.strip()) # 원본에서 \n를 날림.


# 방법2
handle = open(file_name, "r")
for line in handle:
    print(line.strip())
handle.close()


# 방법3
handle = open(file_name, "r")
lines = handle.readlines() # 방법2에서 이 줄이 추가됨.
for line in lines:
    print(line.strip())
handle.close()
