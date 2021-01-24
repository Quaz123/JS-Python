def args(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print("{}: {}".format(key, value))


args("a", "b", key1="c", key2="d")


def person_print(name, last_name, *others, age):
    formatted_data = 'Imię: {}, Nazwisko: {}, Wiek: {}'.format(name, last_name, age)
    others_str = ' '
    for arg in others:
        others_str += arg + ' '
    print(formatted_data + others_str)


person_print('Adam', 'Kowalski', 'a', 'b', age=35)