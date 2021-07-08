with open("title.txt", "r") as fr:
    print("The first line is: ", end="")
    print(fr.readlines()[0])
