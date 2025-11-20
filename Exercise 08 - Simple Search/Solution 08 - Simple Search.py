# Create a list containing several names
name = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Check if 'Sam' is on the list
user = 'Sam'
if user in name:
    print (f'The name {user} is in the list ')
else:
    print (f'The name {user} is NOT in the list ')
    
# Prompt the user to enter a name to search for
user_input = input ('Enter the name to search: ')

# Check if the entered name exist in the list
if user_input.capitalize() in name:
    # If the name is found, print a success message
    print (f'The name {user_input} is in the list ')
else:
    # If the name is not found, print a failure message
    print (f'The name {user_input} is NOT in the list ')