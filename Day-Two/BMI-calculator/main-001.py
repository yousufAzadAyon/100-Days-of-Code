height = float(input('Enter Your Height in M: '))
weight = int(input('Enter Your Weight in KG: '))

bmi = weight / height**2

print(f'\nYour BMI is: {round(bmi)} !')