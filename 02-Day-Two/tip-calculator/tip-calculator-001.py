print('Welcome to the tip Calculator!')

total_bill = float(input('What was the total bill? $'))
tip_percentage = int(input('What persentage of tip you would like to give? 10, 12, or 15? '))
people_number = int(input('How many people to splitt the bill? '))

personal_bill = (total_bill + (total_bill * (tip_percentage/100))) / people_number

print(f'\nEach person sould pay: ${round(personal_bill,2)}')