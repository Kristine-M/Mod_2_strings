# Task 1: Timestamp Extraction
# Write a script that extracts the timestamp from each 
# log entry. Assume that the timestamp is always at the beginning 
# of each line and is enclosed in square brackets (e.g., "[2023-03-15 10:00:00]").
def log_extract(log_entries):
    for entry in log_entries:
        print(entry[:21])
        

# Task 2: Error Identification
# Create a function that scans through the log file and 
# identifies any error messages. Assume that all error messages 
# start with the word "ERROR:". The function should print out each 
# error message with its corresponding timestamp.

def error(log_entries):
    num_error = 0
    for entry in log_entries:
        if entry[:6] == "ERROR:":
            print("Error for timestamp: " + entry[6:])
            num_error += 1
            
    return num_error
            

# Task 3: Log Summary
# Develop a script that creates a summary of the log file, including 
# the total number of entries, the number of error messages, and the 
# number of unique timestamps in the file.
def log_summary(log_entries):
    unqiue = []
    error = error(log_entries)
    total = 0
    for entry in log_entries:
        total += 1
        if entry not in unqiue:
            unqiue.append(entry)
    
    print(f"Total entries: {total} entries")
    print(f"Number of error messages: {error}")
    print("Total unique entries: " + len(unqiue) + " entries")
            
    