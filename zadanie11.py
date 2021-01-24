import os
import random
import string

def rozmiar(file):
    open(file, 'a+')
    return os.stat(file).st_size

def wpisz(file):
    f = open(file, 'a+')
    f.write(''.join(random.choice(letters)))

def wyczysc(a):
    print("wczsc", a)
    suma = rozmiar("file1.txt") + rozmiar("file2.txt") + rozmiar("file3.txt")
    if (suma == 300) and (a == 1):
        open("file2.txt", 'w').close()
        print("Czyszcze 2 dla a = ", a)
    elif (suma == 300) and (a == 2):
        open("file3.txt", 'w').close()
        print("Czyszcze 3")
    elif (suma == 300) and (a == 3):
        open("file1.txt", 'w').close()
        print("Czyszcze 1")

def zamknij(file):
    open(file, 'a+').close()

def main(n):
    global a
    wyczysc(a)
    for i in range(0, int(n)):
        size = rozmiar("file1.txt")
        if size < 100:
            wpisz('file1.txt')
            print("1: ", size)
        else:
            zamknij("file1.txt")
            a = 1
            wyczysc(a)
            size = rozmiar('file2.txt')
            if size < 100:
                wpisz('file2.txt')
                print("2: ", size)
            else:
                zamknij("file2.txt")
                a = 2
                wyczysc(a)
                size = rozmiar('file3.txt')
                if size < 100:
                    wpisz('file3.txt')
                    print("3: ", size)
                else:
                    zamknij("file3.txt")
                    a = 3
        print(a)


a = 0
letters = string.ascii_lowercase
while(1):
    n = input("Podaj ilosc znakow do wpisania: ")
    main(n)
    print(a)
