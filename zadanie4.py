from random import randint
import time

long_list = [randint(0, 3000) for element in range(1000000)]
x = -1

t1 = time.time()
if x in long_list:
    print('Znaleziono liczbę równą -1')
t2 = time.time()
print(t2-t1)

t1 = time.time()
ct = long_list.count(x)
if ct > 0:
    print('Znaleziono', ct, 'liczb równych -1')
t2 = time.time()
print(t2-t1)

t1 = time.time()
ct = 0
for i in long_list:
    if x == long_list[i]:
        ct = ct + 1
if ct > 0:
    print('Znaleziono', ct, 'liczb równych -1')
t2 = time.time()
print(t2-t1)
