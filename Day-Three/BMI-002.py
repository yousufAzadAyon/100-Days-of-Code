height = float(input('Enter your Height in M: '))
weight = int(input('Enter your Weitght in KG: '))

bmi = round(weight / height**2)

if bmi < 18.5:
    print('Your are underweight')
elif bmi < 25:
    print('you are normal weight')
elif bmi < 30:
    print('you are overweight')
elif bmi < 35:
    print('you are obese')
else:
    print('You are clinically obese')