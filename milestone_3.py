import random

def get_random_word():
    word_list = ['apple', 'melon', 'peach', 'orange', 'plum']
    word = random.choice(word_list)
    return word

def check_guess(guess):
    word = get_random_word()
    guess_lowercase = guess.lower()
    if guess_lowercase in word:
        print('Great job, '  + guess + ' is in the word!')
    else:
        print('Sorry, ' + guess + ' is not in word, please try again')

def ask_for_input():
    while True:
        guess = input("Input a single letter:")
        if len(guess) == 1 and guess.isalpha():
            print('Good guess!')
            break
        else:
            print ('Invalid letter. Please, enter a single alphabetical character.')
            guess
    check_guess(guess)

ask_for_input()