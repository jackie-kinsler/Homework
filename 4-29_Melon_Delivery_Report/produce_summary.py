
def print_report_from_daily_file(day_string,text_file):
    """Takes in the name of the day and a delivery log. Returns produce report

    Opens a delivery log. Looks at each line. Takes info about melon type, 
    number, and revenue. Returns this in a produce report
    """
    
    print (day_string)              #Print the day of the log
    delivery_log = open(text_file)      #Open the log file

    for line in delivery_log:
        line = line.rstrip()
        words = line.split('|')     #Split the log file into useful pieces

        melon = words[0]            #First piece is the melon type
        count = words[1]            #Second piece is the melon count
        amount = words[2]           #Third piece is the melon revenue 

        print(f"Delivered {count} {melon}s for total of ${amount}")
    
    delivery_log.close()                #Close the log file 

#Run the function for each day of melon deliveries 

print_report_from_daily_file("Day 1", "um-deliveries-20140519.txt")

print_report_from_daily_file("Day 2", "um-deliveries-20140520.txt")

print_report_from_daily_file("Day 3", "um-deliveries-20140521.txt")
