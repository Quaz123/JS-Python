word = 'ananas'
i = 5
print('Zgadnij słowo!')

while i > 0:
    print('Masz jeszcze', i, 'prób\n')
    a = input()
    if a == word:
        print('Gratulacje!')
        break
    else:
        i = i - 1
        print('Źle')
        if i == 0 :
            print('Koniec gry, nie udało Ci się')
