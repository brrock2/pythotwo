import random

chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
number_of_letters = int(input("Choose amount of letters in password:"))
numbers = "1234567890"
number_of_numbers = int(input("Choose amount of numbers in passwrod:"))
symbols = "!£$%^&*()_+"
number_of_symbols = int(input("Choose amount of symbols in passwrod:"))
password = ""

for c in range(number_of_letters):
    password += random.choice(chars)
for c in range(number_of_numbers):
    password += random.choice(numbers)
for c in range(number_of_symbols):
    password += random.choice(symbols)

print(password)