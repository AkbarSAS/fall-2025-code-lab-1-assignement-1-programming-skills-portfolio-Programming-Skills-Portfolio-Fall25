# Define a function to check if a number is odd or even
def odd_or_even (number):
    if number % 2 == 0: # If the number is divisible by 2, it is even
        return f'The number {number} is even'
    else:
        return f'The number {number} is odd'
 
# Define the main function   
def main():
    # Prompt the user to input a number
    user_input = int(input('Enter a number: '))
    
    # Send the user’s number to the odd_or_even function
    result = odd_or_even(user_input)
    print (result)
    
if __name__ == '__main__':
    main()
