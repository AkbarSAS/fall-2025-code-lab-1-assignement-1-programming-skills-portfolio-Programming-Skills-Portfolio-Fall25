# Define the correct password
correct_password = '12345'

# Max number of attempts
max_attempts = 5
attempts = 0

# Loop until the number of attempts reaches the maximum.
while attempts < max_attempts:
    user_input = input ('Enter your password: ')
    if user_input == correct_password:
        print ('Access Granted')
        break # Break the loop after successful attempt
    else:
        attempts += 1
        # Calculate the remaining attempts
        remaining = max_attempts - attempts
        
        # Display the number of remaining attempts
        print (f'Incorrect password, {remaining} attempt/s left')

else:
    # Alert the authorities after 5 failed attempts
    print ('Login failed, The authorities have been alerted')