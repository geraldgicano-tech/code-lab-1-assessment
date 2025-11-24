days_of_the_month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
# make a dictionary with stored keys and values
month = int(input("Enter the month number: "))
if month in days_of_the_month:
    print(f"Number of days in month {month}: {days_of_the_month[month]}")
    if month == 2:
        leap_year = input("Is it a leap year? (yes/no): ").lower() 
    if leap_year == "yes":

        print("Number of days in February: 29")
    else:
        print("Number of days in February: 28")
else:
    print("Invalid number. pick a month between 1 and 12.")
    # add an else statement to display invalid month numbers

