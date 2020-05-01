
MELON_COST = 1.00 

accounting_log = open("customer-orders.txt")

#look at each line in the log
#separate out the order numer, customer name, /
#melon count, and actual payment
for line in accounting_log:
    line = line.rstrip()
    words = line.split("|")
    number, full_name, melon_count, actual_payment = words

    #calculate the customer's expected payment 
    expected_payment = float(melon_count) * MELON_COST
    
    #determine customer first name
    first_name = full_name.split(" ")[0]

    #for each line in the log, if the customer payment does not equal / 
    #the expected payment, print their name, what they paid, and what / 
    #the expected payment is 
    if expected_payment != float(actual_payment):
        print(f"{first_name} paid ${actual_payment}, expected ${expected_payment:.2f}")

accounting_log.close()