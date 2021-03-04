# Guess the number game
import random
def guessgame(x):
    mysterious_number = random.randint(1,x)
    # print(mysterious_number)
    entered_number = 0
    counter = 0
    name = input('Your Name : ')
    while entered_number!=mysterious_number:
        entered_number = int(input(f'Guess the number between 1 and {x} : '))
        if entered_number <mysterious_number:
            print("Guess high")
        elif entered_number>mysterious_number:
            print('Guess low')
        counter = counter+1
    if counter <=5:
        print(f'Congratulations,{name} have guess the number in just {counter} round')
    elif counter >=6 and counter <=10:
        print(f'{name},You have guess the number in {counter} round')
    elif counter >=11 and counter <=15:
        print(f'{name}, You have guess the number in {counter} round, Good luck next time')
    else:
        print(mysterious_number)
guessgame(20)