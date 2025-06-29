import random

def numtohand(ans):
    a = ''
    if ans == '1':
        a = 'rock'
    elif ans == '2':
        a = 'paper'
    elif ans == '3':
        a = 'scissor'
    return(a)

def genhand():
    randnum = random.randint(1,3)
    b=''
    if randnum == 1:
        b = 'rock'
    elif randnum == 2:
        b = 'paper'
    elif randnum == 3:
        b = 'scissor'
    return(b)

def logic(player,bot):
    outcome = ''
    if player == bot:
        outcome = 'Its a tie'
    elif player=='rock' and bot =='paper':
        outcome = 'Player Loses!'
    elif player=='rock' and bot =='scissor':
        outcome = 'Player Wins!'
    elif player=='paper' and bot =='rock':
        outcome = 'Player Wins!'
    elif player=='paper' and bot =='scissor':
            outcome = 'Player Loses!'
    elif player=='scissor' and bot =='paper':
        outcome = 'Player Wins!'
    elif player=='scissor' and bot =='rock':
            outcome = 'Player Loses!'
    return(outcome)

def main():
    
    
    while True:
        print('Would you like to play a game?')
        print('1. Yes')
        print('2. No')
        print('3. Exit')

        response = input('Choose and option 1-3: ')
        if response == '1':
            print('Okay lets go')
            print('Choose your weapon')
            print('1. rock')
            print('2. paper')
            print('3. scissor')

            ans = input('Choose and option 1-3: ')
            

            a = game(ans)
            print(a)




        elif response == '2':
            print('sad boy noises')
        elif response == '3':
            print('Byeeee')
            break
        else:
            print('You got to choose a valid option')


if __name__ == "__main__":
    main()
