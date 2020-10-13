from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ['Imie', 'Płeć', 'Wiek']
table.add_row(['Aleksandra', 'Kobieta', 22])
table.add_row(['Piotr', 'Mężczyzna', 13])
table.add_row(['Michał', 'Mężczyzna', 45])
table.add_row(['Kinga', 'Kobieta', 34])
table.add_row(['Przemysław', 'Mężczyzna', 38])
table.add_row(['Olaf', 'Mężczyzna', 19])
table.add_row(['Paulina', 'Kobieta', 41])
print(table)
