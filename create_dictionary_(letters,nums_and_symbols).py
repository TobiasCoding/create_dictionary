import itertools
import string

def get_valid_input(prompt, valid_options):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        print(f"Invalid input. Choose one of {', '.join(valid_options)}.")

def generate_characters(include_lower, include_upper, include_numbers, include_symbols):
    characters = ""
    if include_lower:
        characters += string.ascii_lowercase
    if include_upper:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    return characters

# Opciones del usuario
print("Choose character types to include in passwords:")
include_lower = get_valid_input("Include lowercase letters? (y/n): ", ["y", "n"]) == "y"
include_upper = get_valid_input("Include uppercase letters? (y/n): ", ["y", "n"]) == "y"
include_numbers = get_valid_input("Include numbers? (y/n): ", ["y", "n"]) == "y"
include_symbols = get_valid_input("Include symbols? (y/n): ", ["y", "n"]) == "y"

characters = generate_characters(include_lower, include_upper, include_numbers, include_symbols)

if not characters:
    print("Error: You must select at least one character type.")
    exit()

try:
    length = int(input("Enter password length (e.g., 8): "))
    if length <= 0:
        raise ValueError
except ValueError:
    print("Error: Password length must be a positive integer.")
    exit()

# Prefijo y sufijo opcionales
prefix = input("Insert prefix value (optional): ").strip()
suffix = input("Insert suffix value (optional): ").strip()

# Tamaño del bloque para evitar sobrecarga en la RAM
block_size = 100000

# Número total de combinaciones posibles
total_combinations = len(characters) ** length
print(f"Generating {total_combinations} passwords...")

# Generación de contraseñas
password_count = 0
with open("passwords.lst", "w") as file:
    for combination in itertools.product(characters, repeat=length):
        password = prefix + ''.join(combination) + suffix
        file.write(password + "\n")
        password_count += 1

        # Mostrar progreso cada cierto número de contraseñas
        if password_count % block_size == 0 or password_count == total_combinations:
            progress = (password_count / total_combinations) * 100
            print(f"Progress: {progress:.2f}% done", end='\r')

print("\nArchivo 'passwords.lst' created successfully.")
