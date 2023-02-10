i = 100
i = 200

def num(arg=i):
    print(arg)

i = 3

num()
num(i)

def add(a):   
    b = 100
    print(a + b)
a = 9
print(add(a))
add(a)


def sample(a, b):
    return print(a / b)

print('Call sample...')
sample(1, 2)
sample(b=1, a=2)
# sample(b=1, 2)