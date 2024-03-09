# Task 1: Property Format Checker
# You are given a configuration file where each line contains 
# a property and its value separated by an "=" sign. Write a script 
# that checks each line to ensure it follows this format. If a line 
# does not contain an "=" sign or has more than one, print an error 
# message with the line number.

def format(file_config):
    line_num = 0
    for line in file_config:
        line_num += 1
        if line.count("=") > 1 or line.count("=") > 1:
            print("Error on line number " + line_num)

# Task 2: Whitespace Remover
# Modify the script from Task 1 to remove any leading or trailing 
# whitespace from the property names and values.
def format(file_config):
    line_num = 0
    for line in file_config:
        line = line.strip()
        line_num += 1
        if line.count("=") > 1 or line.count("=") > 1:
            print("Error on line number " + line_num)

# Task 3: Duplicate Property Finder
# Extend the script to check for duplicate property names. 
# If a duplicate is found, print out the property name and the 
# line numbers where the duplicates are located.
def format(file_config):
    line_num = 0
    prop_name = []
    for line in file_config:
        line = line.strip()
        line_num += 1
              
        if line.count("=") > 1 or line.count("=") > 1:
            print("Error on line number " + line_num)
        else:
            i = 0
            while line[i] != "=":
                i += 1
            
            for name in prop_name:
                if line[:i] not in prop_name:
                    prop_name.append(line[:i])                   
                else:
                    print(line[:i] + " duplicate found on line " + line_num)
            