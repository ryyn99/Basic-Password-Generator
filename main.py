import random
import string

alphabet = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list (string.punctuation)

pw_length = int(input('How long would you like your password to be?'))
pw_letters = int(input('How many letters do you want in your pw?'))
pw_numbers = int(input('How many numbers do you want in your pw?'))
pw_symbols = int(input('How many symbols do you want in your pw?'))

password_list = []

for character in range(1, pw_letters + 1):
    password_list.append(random.choice(alphabet))

for character in range(1, pw_numbers + 1):
    password_list.append(random.choice(numbers))

for character in range(1, pw_symbols + 1):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

final_pw = ''.join(password_list)
print(f'Your random password is {final_pw}')