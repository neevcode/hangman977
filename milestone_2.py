import random
word_list = ['apple', 'melon', 'peach', 'orange', 'plum']
word = random.choice(word_list)
print(word)

def user_input_guess_letter():
    guess = input("Input a single letter")
    if len(guess) == 1 and guess.isalpha():
        print('Good guess!')
        return guess
    else:
        print ('Oops! That is not a valid input')

user_input_guess_letter()
