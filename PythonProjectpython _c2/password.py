#password generater
import random
import string


def generate_password(length, include_digits=True,
                      include_special_chars=True):
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password
password_length = 12
print("Generated password:", generate_password(password_length))


principal = float(input("Enter principal amount: "))
time = float(input("Enter time: "))
rate = float(input("Enter rate: "))

simple_interest = (principal * time * rate) / 100
amount = principal + simple_interest

print("Simple Interest is:", simple_interest)
print("Total Amount is:", amount)

