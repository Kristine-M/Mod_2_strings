# Task 1: Header Formatter
# Write a script that formats the headers of the report. 
# Each header should be centered, in uppercase, and underlined 
# with "=" characters.

def underline(text):
    print("\u0332".join(text))
    

def header_format(header):
    length = len(header)
    header = header.center(length + 6, "=")
    
    underlined = underline(header)
    
    return underlined
        

# Task 2: Data Alignment
# Format the raw data so that each column is aligned. Assume 
# the data is separated by commas and should be displayed in a 
# table format with each value left-aligned in its column.

def data(raw_data):
    
    rows = raw_data.split('\n')

    for line in rows:
        data = line.split(',')
        format = ' | '.join(value.ljust(10) for value in data)
        print(format)

# Task 3: Report Summary
# At the end of the report, add a summary section that counts 
# the number of data entries and calculates the average value of
# a numeric column.

def summary(raw_data):
    rows = raw_data.split('\n')
    num_entry = 0
    sum = 0
    for line in rows:
        num_entry += 1
        data = line.split(',')
        format = ' | '.join(value.ljust(10) for value in data)
        for val in data:
           if val.isnumeric():
               sum += val 
        print(format)
    
    avg = sum/num_entry  
    print("Number of entry: " + num_entry)
    print("Average value: " + avg)