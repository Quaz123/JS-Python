plik = None
try:
    with open('pliki/1.txt', 'r') as plik, open('pliki/1_kopia.txt', 'w') as kopia:
        for line in plik:
            kopia.write(line)
        plik.close()
        kopia.close()
finally:
    if plik:
        plik.close()
    if kopia:
        kopia.close()
print(plik.closed)
print(kopia.closed)
