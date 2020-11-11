word = 'ananas'

print('Zgadnij słowo!')
for i in range(0, 5):
    print('Masz jeszcze', 5-i, 'prób')
    a = input()
    if a != word:
        print('Źle')
        if i == 4:
            print('Przegrana')
    else:
        print('Gratulacje!')
        break
