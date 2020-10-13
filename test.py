import sys

def f(a, b):
    return a+b

def g(a,b):
    return a*b


print(f(14, 5))
print(g(3,10))

num = 'a'
print(sys.getsizeof(num))