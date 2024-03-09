# Task 1: Input Length Validator
# Write a script that checks the length of the user's 
# first name and last name. Both should be at least 2 
# characters long. If not, print an error message.

def length_validation(first, last):
    if len(first) < 2 and len(last) < 2:
        print("Invalid name length")
        return False
    else:
        print("Valid name")
        return True

# Task 2: Password Complexity Checker
# Create a function that checks the complexity of a user's 
# password. The password must be at least 8 characters long, 
# contain one uppercase letter, one lowercase letter, and one 
# number. If the password does not meet these criteria, print a 
# message explaining the complexity requirements.

def pass_checker(password):
    valid = False
    if len(password) < 8:
        valid = False
        return valid
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
    has_lower = False
    for char in password:
        if char.islower():
            has_lower = True
    has_num = False
    for char in password:
        if char.isnumeric():
            has_num = True
    
    if has_upper and has_lower and has_num:
        return True
    else:
        if not has_upper:
            print("Needs a uppercase letter")
        if not has_lower:
            print("Needs a lowercase letter")
        if not has_num:
            print("Needs a number")
        return False
            
                

# Task 3: Email Formatter
# Implement a script that ensures all user email addresses 
# are in a standard format. Convert the entire email address 
# to lowercase and replace any spaces with a period.

def email(user_email):
    has_amper = False
    for i in range(len(user_email)):
        
        if (i != 0) and (user_email[i] == "@"):
            has_amper = True
            
    has_period = False
    if user_email.count(".") == 1:
        has_period = True
    
    user_email = user_email.tolower()
    
    user_email.replace(" ", ".")
    
    if has_amper and has_period:
        return True
    else:
        return False
    
    