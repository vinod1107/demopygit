# data types
# None - Equivalent to NULL in other languages
# Numeric - int, float, complex(imaginary num -> 6+9j) & bool
# List
# tuple
# set
# string
# range
# dictonary/Map

# a = 6 + 9j
# print(type(a))
# a: float = 5.65
# b = int(a)
# k = 6
# c = complex(b, k)
# print(c)

# Python code to demonstrate the working of
# phase()

# importing "cmath" for complex number operations
import cmath

# Initializing real numbers
# x = -1.0
# y = 0.0
#
# # converting x and y into complex number
# z = complex(x,y);
#
# # printing phase of a complex number using phase()
# print ("The phase of complex number is : ",end="")
# print (cmath.phase(z))
# s = {'first_name': 'Vinod', 'last_name': 'Krishnan'}
# print(s.get('last_name'))
# str = 'Vinod'
# char = 'a'
# print(type(str),' ', type(char))
# print(range(10))
# l = list(range(2,10,2))
# print(l)
# s = {'first_name': 'Vinod', 'last_name': 'Krishnan', 'age': 45}
# # print(s.keys())
# # print(s.values())
# print(s['age'])
# print(s.get('age'))

# import sys
# x = int(sys.argv[1])
# y = int(sys.argv[2])
# z = x + y

# x = 8
# if x % 2 == 0:
#     print('even')
# else:
#     print('odd')
# i = 5
# while i >= 1:
#     print('Hello', end=' ')
#     j = 1
#     while j <= 4:
#         print('world', end=' ')
#         j += 1
#     i -= 1
#     print()
# x = ['vinod', 43, 10.5]
# x = 'Vinod'
# for i in ['Vinod', 43, 10.5]:
#     print(i)
# for i in range(1, 21):
#     if i % 5 != 0:
#         print(i, end=' ')
# x = int(input('How many candies do you want?'))
# i: int = 1
# av: int = 7
# while i <= x:
#     if i >= av:
#         print('candies out of stock')
#         break
#     print('Candy', end='\n')
#     i += 1
# for i in range(1, 21):
#     if i % 3 == 0 or i % 5 == 0:
#         continue
#     print(i, end=' ')
# for i in range(1, 21):
#     if i % 3 == 0 or i % 5 == 0:
#         pass
#     else:
#         print(i, end=' ')
# x: int = 4
# y: int = 4
# for i in range(0, x):
#     print('# ' * y)
# for i in range(1, 5):
#     for j in range(0, i):
#         print('#', end=' ')
#     print()
# for i in range(4, 0, -1):
#     for j in range(0, i):
#         print('#', end=' ')
#     print()
# nums = [12, 26, 36, 8, 11]
#
# for num in nums:
#     if num % 5 == 0:
#         break
# else:
#     print('Value not found')
# from math import sqrt

x = int(input('Enter the prime number range'))
for i in range(2, x + 1):
    count = 0
    for j in range(2, (i // 2 + 1)):
        if i % j == 0:
            count += 1
            break
    if count == 0:
        print(i)
