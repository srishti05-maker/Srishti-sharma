import random
import string

def generate_password(length=12, use_special_chars=True):
    if length < 4:
        return "Password length should be at least 4 characters."

    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation

    # Ensure password has at least one of each type
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation) if use_special_chars else random.choice(string.ascii_letters)
    ]

    # Fill the rest of the password length
    password += random.choices(characters, k=length - 4)
    random.shuffle(password)

    return ''.join(password)

# Example usage
if __name__ == "__main__":
    length = int(input("Enter desired password length: "))
    special = input("Include special characters? (yes/no): ").lower() == 'yes'
    password = generate_password(length, special)
    print(f"Generated password: {password}")