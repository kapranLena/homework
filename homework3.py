word = input('your text')
consonants = 'qwrtpsdfghjklzxcvbnm'

for letter in word:
    if letter in consonants:
        word = word.replace(letter, '')
print(len(word))

""""""

# # my_str = input('your text')
# # my_str2 = my_str.swapcase()
# # print(my_str2, my_str)
# import letter as letter

""""""

from urllib.parse import urlparse

domain = urlparse('https://github.com/carbonfive/test').netloc
print(domain)

""""""

string = input('your text')
print(''.join(filter(str.isupper, string)))

""""""

import random
num = input('pass')
pas = ''
for x in range(16): #Количество символов (16)
    pas = pas + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
print(pas)

import string
import random
characters = string.ascii_letters + string.punctuation  + string.digits

password = ""
password_length = random.randint(8, 16)

for x in range(password_length):
    char = random.choice(characters)
    password = password + char

print(password)
