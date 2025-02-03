import string
import secrets

# Define function "generate_password"
def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    # combine all the variables into one list
    all_characters = letters + digits + symbols
    print("All characters:", all_characters)
    password = ''
    # Generate password
    for _ in range(length):
        password += secrets.choice(all_characters)
    return password
new_password = generate_password(8)

    
    
    
