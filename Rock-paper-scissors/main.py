import random



def main():
    randnum = random.randint(1,3)
    
    while True:
        print('Would you like to play a game?')
        print('1. Yes')
        print('2. No')
        print('3. Exit')

        response = input('Choose and option 1-3: ')
        if response == '1':
            print('Okay lets go')
        elif response == '2':
            print('sad boy noises')
        elif response == '3':
            print('Byeeee')
            break
        else:
            print('You got to choose a valid option')


if __name__ == "__main__":
    main()
