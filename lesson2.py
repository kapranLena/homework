

name = input("Please your name")
if name == "Lena":
   print('Hello', name)

""""""

num1 = input('enter num 1')
num2 = input('enter num 2')
if num1.isdigit() and num2.isdigit():
    print(int(num1) + int(num2))
else:
    print('Invalid')

""""""
x = input('your number')
if x.isdigit():
    x = int(x)
    if x >= 0:
        if (int(x) % 2) == 0:
            print('number is even')
        else:
            print('number os not even')
    else:
        pass
else:
        print("input only integer positive numbers")

""""""

num = input('your number')
if int(num) > 0:
    if int(num) % 2 == 0:
        print('yes')
    else:
        print('no')
else:
    print('not valid')

""""""
n = input('number')
if n.isdigit() and int(n) > 0:
    n = int(n)
    print(int(n) + int(n*n) + int(n**3))
