from random import randint

a = ['Damian', 'Ola', 'Barbara', 'Robert', 'Zygmunt', 'Ewa']
b = [a[i][0] for i in range(len(a))]
print(b)

c = [[randint(0, 10) for i in range(4)] for j in range(5)]
print(c)
