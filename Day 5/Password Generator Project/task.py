import random
#define characters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
#Ask for input
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Generate random characters
passwordLetters = random.choices(letters, k = nr_letters)
passwordSymbols = random.choices(symbols, k = nr_symbols)
passwordNumbers = random.choices(numbers, k = nr_numbers)

#Combining the characters in the order above (easy version)
password = ' '.join(passwordLetters + passwordSymbols + passwordNumbers )
print(password)

#Combining and shuffling characters(hard version)
passwordHard = passwordLetters + passwordSymbols + passwordNumbers
random.shuffle(passwordHard)
#list to string and print
HardPassword = ' '.join(passwordHard)
print(HardPassword)

