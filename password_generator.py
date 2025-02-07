import re
import string
import secrets

# Define function "generate_password"
def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    # combine all the variables into one list
    all_characters = letters + digits + symbols
    #print("All characters:", all_characters)
    while True:
            password = ''
            # Generate password
            for _ in range(length):
                password += secrets.choice(all_characters)
            constraints = [
                 (nums, r'\d'),
                 (lowercase, r'[a-z]'),
                 (uppercase, r'[A-Z]'),
                 (special_chars, rf'[{symbols}]')


            ]
            # Check if password meets constraints
            
            if all(
                     constraint<=len(re.findall(pattern, password))
                     for constraint, pattern in constraints
            ):
                break
    return password
if __name__ == '__main__':            
    new_password = generate_password()
    print('Generated password:', new_password)

    
    
