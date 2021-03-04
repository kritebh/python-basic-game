import random
def mygame():
    user = input(" Enter 'r' for rock,'p' for paper,'s' for scissors : ")
    bot = random.choice(['r','p','s'])
    # print(bot)
    if user == bot:
        return "Game Tie!"

    if win(user,bot):
        return 'Booyah , You Won!!!'

    return 'Sorry Try again'

# function to check whether user is winner or not
def win(user,bot):
    if (user =='r' and bot =='s') or (user=='s' and bot =='p') or (user =='p' and bot =='r'):
        return True
print(mygame())