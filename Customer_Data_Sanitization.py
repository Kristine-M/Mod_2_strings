# Task 1: Code Correction
# You are provided with a script that is supposed to format 
# customer names by ensuring the first letter is uppercase and 
# the rest are lowercase, regardless of how the data was entered. 
# However, the script contains errors. Correct the script so that 
# it functions as intended.

# ^^^ code script was not provided

# task 2
# Write a function that checks a list of email addresses for 
# a SaaS application's user accounts. The function should verify 
# that each email contains an "@" symbol and a "." after it, indicating 
# a valid email format. If an email doesn't meet this criterion, print 
# it out for further review.

def val_email(email_list):
    valid_email = False
    
    for email in email_list:
        for i in range(len(email)):
            if email[i] == "@":
                if email[i + 1] == ".":
                    valid_email = True
                else:
                    valid_email = False
                    print(f"This email: {email} needs further review")
                    
    

# Task 3: Username Generation
# Create a script that generates a username for each 
# new user. The username should be a combination of the 
# first three letters of their first name and the first three 
# letters of their last name. If the name is shorter than three letters, 
# use the full name. Ensure all usernames are in lowercase.