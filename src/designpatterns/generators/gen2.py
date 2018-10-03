from random import randint

def g():
    while True:
        yield ((randint(0,100), randint(0,100)))

def g2():
    inst = g();
    i = 0
    while i < 2:
        yield next(inst)[i]
        i += 1

inst2 = g2()
print(next(inst2))
print(next(inst2))
