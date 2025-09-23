import re          # For using regular expressions to check password rules
import secrets     # For generating cryptographically secure random characters
import string      # Provides sets of characters like letters, digits, punctuation


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    """
    Generate a random password of given length that satisfies certain constraints:
    - nums: minimum number of digits required
    - special_chars: minimum number of special characters required
    - uppercase: minimum number of uppercase letters required
    - lowercase: minimum number of lowercase letters required
    """

    # Define character sets
    letters = string.ascii_letters      # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = string.digits              # '0123456789'
    symbols = string.punctuation        # All punctuation characters

    # Pool of all possible characters to choose from
    all_characters = letters + digits + symbols

    # Keep generating passwords until one meets all the constraints
    while True:
        password = ''
        
        # Build a password character by character
        for _ in range(length):
            password += secrets.choice(all_characters)   # Random secure choice from pool
        
        # Define regex patterns to check constraints
        constraints = [
            (nums, r'\d'),                   # At least `nums` digits (\d means digit)
            (special_chars, fr'[{symbols}]'),# At least `special_chars` special characters
            (uppercase, r'[A-Z]'),           # At least `uppercase` capital letters
            (lowercase, r'[a-z]')            # At least `lowercase` small letters
        ]

        # Verify all constraints using regex counts
        # re.findall(pattern, password) → list of all matches
        # len(...) gives number of matches
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            # If all constraints satisfied, break out of loop
            break
    
    # Return the valid password
    return password


# Only run the following if the script is executed directly
if __name__ == '__main__':
    new_password = generate_password()   # Generate password with default rules
    print('Generated password:', new_password)  # Print result to user
