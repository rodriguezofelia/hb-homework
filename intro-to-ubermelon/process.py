#File created in order to access it 
log_file = open("um-server-01.txt")

#Function definition 
def sales_reports(log_file):
    """Returns line item that begin with 'Mon'"""

    #For each line in log_file
    for line in log_file:

        #Removes whitespace at end of string
        line = line.rstrip()

        #Slices string to include the first three characters
        day = line[0:3]

        #Will print all lines that start with 'Mon' 
        if day == "Mon":
            print(line)

#Calls sales_reports and passes log_file as the argument 
sales_reports(log_file)
