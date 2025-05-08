import random

def generate_password(length, use_letters, use_numbers, use_symbols):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?/'

    characters = ''
    if use_letters:
        characters += letters
    if use_numbers:
        characters += numbers
    if use_symbols:
        characters += symbols

    if characters == '':
        return "Error: No character types selected."

    password = ''
    for _ in range(length):
        password += random.choice(characters)

    return password

# Main Program
print("=== Password Generator ===")
try:
    length = int(input("Enter password length: "))
except ValueError:
    print("Invalid input. Length must be a number.")
    exit()

use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

result = generate_password(length, use_letters, use_numbers, use_symbols)
print("\nGenerated Password:", result)
