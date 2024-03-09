# Task 1: Command Parser
# Write a script that takes a user's text input 
# and identifies if it contains one of the predefined 
# commands (e.g., "help", "issue", "contact support"). 
# If a command is found, print a response related to the command.

text = input("What do you need assistance in? ")

def command(text):
    words = ["help", "issue", "contact support"]
    
    for keyword in words:
        if keyword in text:
            if keyword == "help":
                print("What do you need help on?")
            if keyword == "issue":
                print("What seems to be the issue?")
            if keyword == "contact support":
                print("What do you need support on?")
                
# Task 2: Issue Categorizer
# If the user's input contains the word "issue", further
# categorize the issue based on keywords such as "login", 
# "performance", "error", etc. Print out the category of the
# issue for the support team.

def issue_cater(text):
    words = ["help", "issue", "contact support"]
    issue_list = ["performance", "error", "login"]
    
    for keyword in words:
        if keyword in text:
            if keyword == "help":
                print("What do you need help on?")
            if keyword == "issue":
                for word in issue_list:
                    if word in text:
                        if word == "performance":
                            print("Category: " + word)
                        if word == "error":
                            print("Category: " + word)
                        if word == "login":
                            print("Category: " + word)
            if keyword == "contact support":
                print("What do you need support on?")

# Task 3: Auto-Response Generator
# For general help inquiries, create a script that generates 
# an auto-response providing links to the FAQ section, support
# contact information, and a link to submit a ticket.

inquire = input("What is you question?")
print("That is a great question, please refer to our FAQ using this following link: www.FAQ.com")
print("If you have a more specific question, please contact our tech support at techsupport@gmail.com, or sumbit a support ticket here www.ticket.com.")