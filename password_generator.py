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
                 (nums, '')
            ]
            return password
        # new_password = generate_password(8)
        # print(new_password)
pattern = re.compile('i')
quote = 'Not all those who wander lost'
print(pattern.search(quote))
    
    
