import random
import string

print("===== Random Password Generator =====")

while True:
    # Password length
    while True:
        try:
            length = int(input("Enter password length (minimum 8): "))
            if length >= 8:
                break
            else:
                print("Password length must be at least 8.")
        except ValueError:
            print("Please enter a valid number.")

    # Character type selection
    use_upper = input("Include Uppercase Letters? (y/n): ").lower()
    use_lower = input("Include Lowercase Letters? (y/n): ").lower()
    use_digits = input("Include Numbers? (y/n): ").lower()
    use_symbols = input("Include Symbols? (y/n): ").lower()

    characters = ""
    password = []
    selected_types = 0

    if use_upper == "y":
        characters += string.ascii_uppercase
        password.append(random.choice(string.ascii_uppercase))
        selected_types += 1

    if use_lower == "y":
        characters += string.ascii_lowercase
        password.append(random.choice(string.ascii_lowercase))
        selected_types += 1

    if use_digits == "y":
        characters += string.digits
        password.append(random.choice(string.digits))
        selected_types += 1

    if use_symbols == "y":
        characters += string.punctuation
        password.append(random.choice(string.punctuation))
        selected_types += 1

    # Validation
    if selected_types < 2:
        print("\nError: Please select at least TWO character types.\n")
        continue

    # Fill remaining characters
    while len(password) < length:
        password.append(random.choice(characters))

    # Shuffle password
    random.shuffle(password)

    # Display password
    final_password = "".join(password)
    print("\nGenerated Password:")
    print(final_password)

    # Generate another?
    again = input("\nGenerate another password? (y/n): ").lower()
    if again != "y":
        print("Thank you for using the Password Generator!")
        break