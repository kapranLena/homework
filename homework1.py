
x = input('What is the input string?')
len(x)
if len(x) != 0 :
    print(len(x))
else:
    print('write something')

""""""

num1 = input('number 1')
num2 = input('number 2')
if num1.isdigit() and num2.isdigit():
    n1 = int(num1)
    n2 = int(num2)
    if int(num1) > 0 and int(num2) > 0:
        print(n1 + n2, n1 - n2, n1 / n2, n1 ** 2)
else:
     print('only integer and positive numbers')


""""""

x = input('how many people?')
y = input('how many pizzas do you have?')
if x.isdigit() and y.isdigit():
    m = (int(y) * 8) // int(x)
    l = int(x) * m
    k = (int(y) * 8) - l
    print('each person gets', m, 'pieces of pizza', 'There are', k, 'leftover pieces')
else:
    print('only integer and positive numbers')

""""""
x  = input('currency')
x1 = input('name of currency')
y = float(input('exchange rate'))
z1 = input('name of currency2')
if x.isdigit():
    z = int(x) * y
    print('you can buy', z, x1, 'at the exchange rate', y, 'for', z, z1)

""""""
a = input('Heads')
b = input('Tails')
import random
x = ['a','b']
print(random.choice(x))
if random.choice(x) != a:
    print('you win')
else:
    print('you lose')