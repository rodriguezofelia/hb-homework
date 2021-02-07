def melons_sold_by_salesperson(sales_report):
    """ Returns a dictionary of salesperson along with melons_sold """

    total_melons_sold_by_salesperson = {}

    file = open('sales-report.txt')
    for line in file:
        line = line.rstrip()
        # Will create list of data and unpack the values 
        salesperson, _, melons_sold = line.split('|')
        
        # Will create or add to the salesperson's total melon sold count
        if salesperson not in total_melons_sold_by_salesperson:
            total_melons_sold_by_salesperson[salesperson] = int(melons_sold)
        else:
            total_melons_sold_by_salesperson[salesperson] += int(melons_sold)
        
    return total_melons_sold_by_salesperson


def print_sales_report(total_melons_sold_by_salesperson):
    """ Prints a report of the salespeople and the total number of melons they've sold """

    for salesperson, melons_sold in total_melons_sold_by_salesperson.items():
        print(f'{salesperson} sold {melons_sold} melons')


print_sales_report(melons_sold_by_salesperson("sales-report.txt"))