import random
run_game = True
min_num = int(input('enter minimum Number: '))
max_num = int(input('enter the maximum Number: '))
guess_limit = 4

while run_game:

    number = random.randint(min_num , max_num)

    guess_limit -= 1
    if guess_limit == 0:
        run_game = False

    print('-----'*9)
    guessed_number = int(input('Enter Your Guess: '))
    print('-----'*9)

    if guessed_number == number:
        print(f'The Random Number was {number} and You Entered {guessed_number}.')
        print('Congratulations!!! You have guessed it right!\n')
        print('-----'*9)

    elif guessed_number < number:
        print(f'the number is {number} and you entered {guessed_number}')
        print('Sorry! Try again!')
        print('-----'*9)

    elif guessed_number > number:
        print(f'The number is {number} and you entered {guessed_number} !')
        print('Sorry! Try Again!')
        print('-----'*9)

    else:
        print('Invalid Input!!!\n Try Again!')
        print('-----'*9)
    
print("Sorry! You ran out chances!\n")