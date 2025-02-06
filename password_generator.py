import re
import string
import secrets

# Define function "generate_password"
def generate_password(length, nums, special_chars, uppercase, lowercase):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    # combine all the variables into one list
    all_characters = letters + digits + symbols
    print("All characters:", all_characters)
    while True:
            password = ''
            # Generate password
            for _ in range(length):
                password += secrets.choice(all_characters)
            constraints = [
                 (nums, r'\d'),
                 (lowercase, r'[a-z]'),
                 (uppercase, r'[A-Z]')
                 (special_chars, rf'[{symbols}]')


            ]
            # Check if password meets constraints
            count = 0
            for constraint, pattern in constraints:
               if constraint <= len(re.findall(pattern, password)):
                count+=1
            if count == 4:
                break

    return password
            
        # new_password = generate_password(8)
        # print(new_password)

    
    
