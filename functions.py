from functools import *


def greet():
    print('Hello', end=' ')
    print('Good Morning')


def add(x, y):
    c = x + y
    return c


def add_sub(x, y):
    a = x + y
    b = x - y
    return a, b


# result1, result2 = add_sub(5, 4)
# print(result1, end=' ')
# print(result2)
def update(x):
    x = 8
    print('x', '=', x)


def change(lst):
    lst[1] = 25
    print('inside:', lst)


# lst = [10, 20, 30]
# change(lst)
# print('outside:', lst)

# a = 10
# update(a)
# print('a', '=', a)

def person(name, age=18):
    print(name)
    print(age)


# person(age=43, name='Vinod')
# person('Vinod', 43)

def sum(a, *b):
    c = a
    for i in b:
        c = c + i
    return c


# value = sum(4, 5, 6, 7, 8)
# print(value)

def person_det(name, **b):
    print(name)
    for i, j in b.items():
        print(i, j)


# person_det('Vinod', age=43, city='Trichy', phone=9876543210)

g_a = 10
g_b = 11


# def g_change():
#     global g_a
#     g_a += 1
#     print(g_a)
#
#
# g_change()
def g_change():
    g_a = 10
    print(g_a)
    globals()['g_a'] += 1


# g_change()
# print(g_a)
def count(lst):
    count_even = 0
    count_odd = 0
    for i in lst:
        if i % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    return count_even, count_odd


# lst = [22, 24, 35, 66, 77, 89, 92]
# count_even, count_odd = count(lst)
# # print('even count:', count_even, 'count_odd:', count_odd)
# print('Even: {} and odd: {}'.format(count_even, count_odd))
def fib(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(n + 1):
        c = a + b
        a = b
        b = c
        print(c)


# fib(15)
def fact(n):
    fac = 1
    for i in range(n, 0, -1):
        fac = fac * i
    return fac


# fac = fact(5)
# print(fac)
def fac_rec(n):
    if n <= 1:
        return 1
    return n * fac_rec(n - 1)


# fac = fac_rec(5)
# print(fac)
# f = lambda a, b: a + b
# result = f(5, 6)
# print(result)
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evens = list(filter(lambda n: n % 2 == 0, nums))
# print(evens)
# doubles = list(map(lambda n: n * 2, evens))
# print(doubles)
# sums = reduce(lambda a, b: a + b, doubles)
# print(sums)

