"""Generate sales report showing total melons each salesperson sold."""

#create an empty list of sales people
#because theyre unique
salespeople = []

#create an empty list of melons sold 
melons_sold = []

# opens sales-report.txt, reads in each line
# for each line, the line is stripped of leading and trailing whitepsace
# the items on the line are split by the | and added to a list 
f = open('sales-report.txt')
for line in f:
    line = line.rstrip()
    entries = line.split('|')

    # assigns 1st item of list (names of salesperson) to 'salesperson'
    salesperson = entries[0]
    # assigns 3rd item of list (number of melons) to 'melons'
    melons = int(entries[2])

    # If the salesperson is in the salespeople list, position becomes the 
    # index value of that salesperson (note, this will cause an issue with 
    # repeated list values)
    if salesperson in salespeople:
        position = salespeople.index(salesperson)

        # adds the numer of melons at the salesperson's index to the existing 
        # number of melons in the corresponding melon list 
        melons_sold[position] += melons
    else:
        # adds the salespersons name to the end of the salespeople list
        salespeople.append(salesperson)
        # adds the melons to the end of the melons_sol list 
        melons_sold.append(melons)

#prints out the salespersons name and melon count 
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')

#IMPROVEMENT would be to use a dictionary - then the salesperson names would be
# forced to be unique. Additionaly, would solve indexing issues. 
# Would also solve issue of having two lists that are not linked togther
