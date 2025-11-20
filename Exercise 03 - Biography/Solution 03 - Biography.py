# Ask the user to enter their name
name = input ('Enter your name: ')
# Ask the user to enter their hometown
home_town = input ('Enter your hometown: ')
# Ask the user to enter their age
age = input('Enter your age (in numbers): ')

# store the user details in a dictionary
biography = {'name' : name,
             'hometown' : home_town,
             'age' : age}

# Check if the age input is numeric
while not age.isdigit():
    print ('Please enter a valid number')
    age = input('Enter your age (in numbers): ')
    biography['age'] = age

# print each user detail on a new line using f'string
print (f"Name: {biography['name']} \nHometown: {biography['hometown']} \nAge: {biography['age']}")