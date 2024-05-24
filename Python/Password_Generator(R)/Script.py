# Imports
import random

# Variables
upper_case_array = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                    "U", "V", "W", "X", "Y", "Z"]
lower_case_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z"]
numbers_array = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
chars_array = ["@", "#", "$", "*"]
password_array = ["", "", "", "", "", "", "", ""]
raw_password = ""

# Solving

# Adding uppercase letters
for num1 in range(4):
    letter_index = random.randint(0, 25)
    password_array.insert(random.randint(0, 7), upper_case_array[letter_index])

# Adding lowercase letters
for num2 in range(4):
    letter_index = random.randint(0, 25)
    password_array.insert(random.randint(0, 7), lower_case_array[letter_index])

# Adding numbers
for num3 in range(4):
    letter_index = random.randint(0, 9)
    password_array.insert(random.randint(0, 7), numbers_array[letter_index])

# Adding characters
for num4 in range(4):
    letter_index = random.randint(0, 3)
    password_array.insert(random.randint(0, 4), chars_array[letter_index])

# Forming raw stringed password
for part in password_array:
    raw_password += part

print("This is your password " + raw_password)