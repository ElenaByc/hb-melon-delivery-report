
def print_day_delivery_report(input_file, delivey_day):
    """Produce delivery report for the given day from the given file with data"""

    # Ali Baba Watermelon|18|25.00
    print(f"Day {delivey_day}")
    delivery_data = open(input_file)

    for line in delivery_data:
        melon, count, amount = line.rstrip().split('|')
        print(f"Delivered {count} {melon}s for total of ${amount}")
        
    delivery_data.close()



print_day_delivery_report("um-deliveries-day-1.txt", 1)
print_day_delivery_report("um-deliveries-day-2.txt", 2)
print_day_delivery_report("um-deliveries-day-3.txt", 3)
