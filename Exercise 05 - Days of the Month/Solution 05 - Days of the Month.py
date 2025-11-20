# Create a dictionary with months and number of days
calendar = { 1 : 31, 
            2 : 28,
            3 : 31,
            4 : 30,
            5 : 31,
            6 : 30,
            7 : 31,
            8 : 31,
            9 : 30,
            10 : 31,
            11 : 30,
            12 : 31}

# Loop until the user gives a valid month
while True:
    # Ask the user for a month number
    month = int(input("Enter month number (1-12): "))
    
    if month in calendar:
        break # Close the loop after a valid input
    else:
        print("Error, please enter a number (1 - 12)")


# Check if the month is February
if  month == 2:
    
    while True:
            # Ask the user if it is a leap year
        leap_year = input('Is it a leap year (Yes/No): ').lower()
        
        if leap_year == 'yes':
            print ('February has 29 days')
            break
        
        elif leap_year == 'no':
            print ('February has 28 days')
            break
        
        else:
            print ('Please answer (yes or no)')
                
else:
    # Display the month and number of days
    print (f'The month {month} has {calendar[month]} days')