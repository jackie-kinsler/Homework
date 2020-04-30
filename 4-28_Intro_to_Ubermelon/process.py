#opens a log_file with the sales information from the week. Each sale is dated.
log_file = open("um-server-01.txt")

#defines a function that takes the log_file as the input
def sales_reports(log_file):
    for line in log_file:   
        line = line.rstrip()    #removes the leading spaces in the log file
        day = line[0:3]         #Defines the first three characters of the line as 'day' 
        if day == "Mon":        #If 'day' is 'Mon', the line is printed
            print(line)

#this will print all monday sales 
sales_reports(log_file)

