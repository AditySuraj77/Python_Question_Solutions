print('Generators in Python')

def gen(n):
    yield n**2

x = gen(5)
print(x.__next__())
print(type(x))