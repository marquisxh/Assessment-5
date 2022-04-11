log_file = open("um-server-01.txt") # variable that equals opening the txt file


def sales_reports(log_file): #This is a function line being initiated
    for line in log_file: #This is a for loop
        line = line.rstrip() #removing whitespace from end of the line
        day = line[0:3] # setting a day that's equal to the first three characters 
        if day == "Mon": # if the day is a specific day
            print(line) # print the line


sales_reports(log_file) # print all lines with specific day
