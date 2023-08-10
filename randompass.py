import random
import string

def generate_password(length, use_lowercase, use_uppercase, use_digits, use_special, custom_special_chars):
    characters = ""
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    if custom_special_chars:
        characters += custom_special_chars

    if not characters:
        print("Error: You must select at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_passwords_to_file(passwords, filename):
    with open(filename, 'w') as file:
        for password in passwords:
            file.write(password + '\n')

def main():
    print("Welcome to the Enhanced Password Generator!")
    num_passwords = int(input("Enter the number of passwords to generate: "))
    length = int(input("Enter the desired length of each password: "))
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include standard special characters? (y/n): ").lower() == 'y'
    custom_special_chars = input("Enter any custom special characters to include (or press Enter for none): ")

    passwords = []
    for _ in range(num_passwords):
        password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special, custom_special_chars)
        if password:
            passwords.append(password)

    if passwords:
        print("\nGenerated Passwords:")
        for i, password in enumerate(passwords, start=1):
            print("Password {}: {}".format(i, password))

        save_to_file = input("\nDo you want to save these passwords to a file? (y/n): ").lower() == 'y'
        if save_to_file:
            filename = input("Enter the filename to save the passwords to: ")
            save_passwords_to_file(passwords, filename)
            print("Passwords saved to", filename)

if __name__ == "__main__":
    main()

