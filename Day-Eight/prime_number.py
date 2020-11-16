def prime_number(number):
    is_prime = True

    for i in range(2,number-1):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print(f'{number} is a Prime Number!')
    else:
        print(f'{number} is not Prime Number!')

number = int(input('Enter a Number: '))
prime_number(number)