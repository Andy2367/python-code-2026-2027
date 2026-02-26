'''
04/09/2025
Andy Cowie
Rock papaer scissors with Error handeler
'''

def determin_winer(player,computer):
    if player == computer:
       return('It is a tie')
    elif(player == "rock" and computer == "scissors") or (player == "scissors" and computer == "paper") or (player == "paper" and computer == "rock"):
        return("you win")
    else:
        return('computer wins.')

while True:
    try:
        import random
    #function to determin winer.
        choices=['rock', 'paper', 'scissors']

    #main game loop.

       
        print ('rock, paper, scissors game!')
        player_choice= input('enter your choice(rock, paper, scissors or quit to exit!)').lower()
        player_choice=player_choice.strip().replace(" ", "")  #join
        print (player_choice)
        '''
        if player_choice not in choices:  # raises Type error and trows to except
            raise TypeError
        
        computer_choice=random.choice(choices)
        print (f'computer choses {computer_choice}.')
        result = determin_winer (player_choice, computer_choice)
        print(result)
        if player_choice == "quit":
           print("thank's for playing")
           break
'''
    except:
        print("somthing went wrong. Maybe you entered a number instead of text? Pleas try again") # makes program not go splat

    finally:
        print ("thanks for playing :)") # happens regardles
        