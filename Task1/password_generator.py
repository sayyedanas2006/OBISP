import random
import string

print("=== Password Generator ===")

# ---------- Password Length ----------
while True:
    user_input = input("Password length (8-20): ")

    if user_input.isdigit():
        length = int(user_input)
        if 8 <= length <= 20:
            break
        else:
            print("❌ Please enter a number between 8 and 20.")
    else:
        print("❌ Please enter numbers only.")

# ---------- Yes / No Input Function ----------
def yes_no_input(msg):
    while True:
        choice = input(msg + " (y/n): ").lower()
        if choice in ["y", "n"]:
            return choice == "y"
        else:
            print("❌ Please enter y or n only.")

upper = yes_no_input("Include Uppercase letters?")
lower = yes_no_input("Include Lowercase letters?")
digits = yes_no_input("Include Digits?")
symbols = yes_no_input("Include Symbols?")

# ---------- Character Selection ----------
chars = ""
if upper:
    chars += string.ascii_uppercase
if lower:
    chars += string.ascii_lowercase
if digits:
    chars += string.digits
if symbols:
    chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"

# ---------- Validation ----------
if not chars:
    print("❌ Error: You must select at least one character type!")
    exit()

# ---------- Password Generation ----------
password = "".join(random.choice(chars) for _ in range(length))

print("\n✅ Generated Password:")
print(password)
