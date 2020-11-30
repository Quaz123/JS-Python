plik = open('pliki/1.txt', 'w+')
plik.write('test')
plik = open('pliki/1.txt')
print(plik.read())
