def person_print(name, last_name, age, *others):
    formatted_data = 'Imię: {}, nazwisko: {}, wiek: {}'.format(name, last_name, age)
    others_str = ' '
    for arg in others:
        others_str += arg + ' '
    print(formatted_data + others_str)


person_print('Adam', 'Kowalski', 35, 'a', 'b')


def iloczyn(*a):
    wynik = 1
    for i in a:
        wynik = wynik * i
    print("Wynik:", wynik)


iloczyn(1, 4, 6, 32)


def wizytowka(**dane):
    for key, value in dane.items():
        print("{}: {}".format(key, value))


wizytowka(Imie="Adam", Nazwisko="Kowalski", Wiek=35)
