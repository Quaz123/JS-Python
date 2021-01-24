try:
    with open("pliki/1.txt", "r") as readFile:
        with open("pliki/1_kopia.txt", "w") as writeFile:
            writeFile.writelines(readFile.readlines())
except IOError as e:
    print(e)
