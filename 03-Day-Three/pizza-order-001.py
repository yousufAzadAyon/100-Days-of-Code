print('Welcome to random pizza delivery!')
size = input('What size pizza do you want? S,M,L?\n:').upper()
bill = 0

if size == 'S':
    bill = 15
elif size == 'M':
    bill = 20
elif size == 'L':
    bill = 25

print(f'Your bill is {bill}')
pepperoni = input('Do you want extra Pepperoni?Y/N?\n:').upper()
if pepperoni == 'Y' and size == 'S':
    bill += 2
elif pepperoni == 'Y' and size != 'S':
    bill += 3

cheese = input('Do you want extra cheese? N/Y?\n:').upper()
if cheese == 'Y':
    bill += 1

print(f'Your final bill is ${bill}')