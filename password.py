import random
print ("Welcome to the PyPassword Generator!")
password = ""

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
 'u', 'v', 'w', 'x', 'y', 'z']


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


symbols = ['@', '#', '$', '%', '&', '*', '+', '-', '=', '/',
 '\\', '|', '^', '~', '<', '>', '(', ')', '[', ']',
 '{', '}', ':', ';', ',', '.', '_', '`']

input_letters = int(input("How many letters would you like in your password?\n"))
lett = [random.choice(letters) for i in range(int(input_letters))]
password += ''.join(lett)

input_symbol=int(input("How many symbols would you like?\n"))
symb = [str(random.choice(numbers)) for i in range(int(input_symbol))]

password += ''.join(symb)

input_numbers=int(input("How many numbers would you like?\n"))
numb = [random.choice(symbols) for i in range(int(input_numbers))]
password += ''.join(numb)
passwords = ''.join(random.sample(password, len(password)))
print(f"Your password is: {passwords}")

