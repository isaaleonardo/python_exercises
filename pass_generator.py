import string
import random

# Function to ask a question and receive either just `yes` or `no`
def ask_question(question: str):
    while True:
        answer = input(f"{question} -> ").lower()
        if (answer == "yes" or answer == "no"):
            return answer
        else:
            print("Please type 'yes' or 'no'")

# Declaring possible characters of password
uppercase_alphabet = list(string.ascii_uppercase)
lowercase_alphabet = list(string.ascii_lowercase)
symbols = ["!", "?", "#", "@", "$", "%", "&", "/", "*"]
digits = list(range(0, 10))

for i in digits:
    digits[i] = str(i)

# Recognizing user decisions about the password
boolean_upper_lowercase = ask_question("Do you want the password to include both upper and lower case letters?")
boolean_digits = ask_question("Do you want the passwork to include numbers?")
boolean_symbols = ask_question("Do you want the password to include symbols?")
while True:
    try:
        size = int(input("How many characters do you want the password to have? -> "))
        break
    except ValueError:
        print("Please input an integer number only...")  

# Generating the password
## Setting all characters available for password and including one of every type into the password
characters = lowercase_alphabet
password = []
password.append(random.choice(lowercase_alphabet))
characters_type = 0

if(boolean_upper_lowercase == 'yes'):
    characters = characters + uppercase_alphabet
    password.append(random.choice(uppercase_alphabet))
    characters_type += 1

if(boolean_digits == 'yes'):
    characters = characters + digits
    password.append(random.choice(digits))
    characters_type += 1

if(boolean_symbols == 'yes'):
    characters = characters + symbols
    password.append(random.choice(symbols))
    characters_type += 1

## Including characters left needed
for i in range(0, int(size) - characters_type):
    password.append(random.choice(characters))

random.shuffle(password)

print("Your password is:")
print("".join(password))