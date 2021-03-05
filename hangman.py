import random
from words_for_hangman import words
import string

def mygame():
    word = random.choice(words).upper()
    lives = 6 
    # print(word)
    letters_in_word = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    while len(letters_in_word) > 0 and lives >0:
        print('You have used these letters',''.join(used_letters),'and',lives,' lives left')
        created_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current Word',''.join(created_list))
        user_letter = input('Guess a letter : ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in letters_in_word:
                letters_in_word.remove(user_letter)
            else:
                lives = lives-1
                print('Letter is not in the word')
        elif user_letter in used_letters:
            print('You have used this letter')

        else:
            print('Wrong Character')
    print(word)

user_word = input('Enter a letter : ')

mygame()