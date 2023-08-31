# x = int(input('Enter a Number'))
# y = int(input('Enter another number'))
# print(x + y)

# ch = input('Enter a character')
# print(ch[0])
# ch = input('Enter a character')[0]
# print(ch)
# result = eval(input('enter an expression'))
# print(result)

age = int(input('Enter the age'))
if age >= 80:
    print('Super Senior', end=' ')
elif 60 <= age < 80:
    print('Senior', end=' ')
else:
    print('Ordinary', end=' ')
print('Citizen')