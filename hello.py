#hello.py

a = 1
b = 1

if a > 1:
    print('big')
    print('big')
    print('hello world')

    for i in range(1,10):
        print(i)

print('end')


def add(m, n):
    s = m
    s += n
    return s


def mymax(m, n):
    if m > n:
        return m
    else:
        return n


