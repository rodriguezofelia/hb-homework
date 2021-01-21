#Function defintion 
def delivery_report(day, file_path):
    """ Returns a delivery report for the given day(s) and file(s) """

    # Prints the day that is passed in 
    print(day)
    # Opens the file that is passed in
    the_file = open(file_path)

    for line in the_file:

        # Removes whitespace at end of string
        line = line.rstrip()
        
        # Will split the line at the specified separator 
        words = line.split('|')
       
        # Returns the given indexes
        melon = words[0]
        count = words[1]
        amount = words[2]

        # Prints the message based on the variables detailed above
        print(f"Delivered {count} {melon}s for total of ${amount}")
    the_file.close()

# Returns report based on arguments that are passed in
delivery_report("Day 1", "um-deliveries-20140519.txt")
delivery_report("Day 2", "um-deliveries-20140520.txt")
delivery_report("Day 3", "um-deliveries-20140521.txt")
