from operator import index
import random
fruits = ['apple', 'melon', 'peach', 'orange', 'plum']

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for ch in self.word] ## Need to add a while loop here or smth so they change to letter when guessed ##
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess_lowercase = guess.lower()
        if guess_lowercase in self.word:
            print('Great job, ' + guess + 'is in the word!')
            for ch in self.word in enumerate(self.word):
                if ch == guess_lowercase:
                    self.word_guessed[index] = guess_lowercase        
            self.num_letters -= 1                
        else:
            self.num_lives -= 1
            print("Sorry, {letter} is not in the word.")
            print("You have {num_lives} lives left.")
       
    
    def ask_for_input(self):
        while True:
            guess = input("Input a single letter:")
            if len(guess) != 1 or guess.isalpha() == False:
                print ('Invalid letter. Please, enter a single alphabetical character.')
                continue
            if guess in self.list_of_guesses:
                print('You already tried that letter!')
                continue
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

#Testing the code
test = Hangman(fruits)
test.ask_for_input()



