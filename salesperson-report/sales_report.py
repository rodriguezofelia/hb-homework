"""Generate sales report showing total melons each salesperson sold."""


salespeople = []
melons_sold = []

# Opens the file that is passed in 
f = open('sales-report.txt')
for line in f:
    # Removes whitespace at end of string
    line = line.rstrip()
    # Will split the line at the specified separator 
    entries = line.split('|')

    # Get the salesperon and number of melons they've sold
    salesperson = entries[0]
    melons = int(entries[2])

    # Will return index of salesperon if they are already in salespeople and 
    # add the number of melons to the melons_sold at that given index.
    # If the salesperson is not in salespeople, it will append them to salespeople
    # and append the melons as well 
    if salesperson in salespeople:
        # Find index of salesperson in salespeople 
        position = salespeople.index(salesperson)
        # Use the same index to get into melons_sold 
        melons_sold[position] += melons
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

# Prints the given salesperson and melons sold at given index
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')


# Recommendations
# This would be better suited to utilize a dictionary where you could return the total melons sold by a salesperon 
# Additionally, writing functions would also make this easier to follow 1) get the melons sold by salesperson and another to print the report
