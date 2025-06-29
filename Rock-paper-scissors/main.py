import random

def game(ans):
    randnum = random.randint(1,3)
    a = ''
    if ans == '1':
        a = 'rock'
    elif ans == '2':
        a = 'paper'
    elif ans == '3':
        a = 'scissor'
    
    return a





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
