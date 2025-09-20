# welcome to password strength checker
# given password is said to be strong if it satisfy 5 things
# 1. length
# 2. lowercase
# 3. uppercase
# 4. digits
# 5. special_characters

import string
def password_strength(password):
    strength = 0

    # checking for password length
    if len(password) >= 8:
        strength += 1
    else:
        print("you should increase length to 8 characters long")
        
    # checking for lowercase letters
    if any(char in string.ascii_lowercase for char in password):
        strength += 1
    else:
        print("you should include atleast one lower_case letters")
        
    # checking for uppercase letters
    if any(char.isupper() for char in password):
        strength += 1
    else:
        print("you should include atleast one upper_case letters")
        
    # checking for digits
    for char in password:
        if char in string.digits:
            strength += 1
            break
    else:
        print("you should include atleast one digit")
        
    #checking for special characters
    if any(char in string.punctuation for char in password):
        strength += 1
    else:
        print("you should include atleast one special character")
        
    # determining the strength of the password
    if strength == 5:
        return "Strong"
    elif strength <3:
        return "weak"
    else:
        return "moderate"
password = input("Enter your password to check it's strength: ")
result = password_strength(password)
print("your password strength: ",result)


