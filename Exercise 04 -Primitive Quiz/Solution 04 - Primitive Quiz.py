# Define a function called quiz
def quiz (country, answer):
    
    # Print the question for the capital of a country
    print (f'What is the capital of {country}') 
    
    # Ask the user for the answer
    user_answer = input ('Enter your answer: ')
    
    # compare both user answer and the correct answer in lowercase
    if user_answer.lower() == answer.lower():
        print ('Congrats, that was correct')
    else:
        # Display the correct answer if the user guess is wrong
        print (f'Oops! {answer} was the right answer')
 
# Call the quiz function with different countries and capitals       
quiz ('France', 'Paris')
quiz ('Germany', 'Berlin')
quiz ('UK', 'London')
quiz ('Italy', 'Rome')
quiz ('Spain', 'Madrid')
quiz ('Portugal', 'Lisbon')
quiz ('Norway', 'Oslo')
quiz ('Ireland', 'Dublin')
quiz ('Greece', 'Athens')
quiz ('Austria', 'Vienna')
