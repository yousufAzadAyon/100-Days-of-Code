row1 = ['🟪','🟪','🟪']
row2 = ['🟪','🟪','🟪']
row3 = ['🟪','🟪','🟪']

map = [row1, row2, row3]

print(f'{row1}\n{row2}\n{row3}')
position = input('where do you want to put the treasure?\n:')

horizonal = int(position[0])
vertical = int(position[1])

map[vertical-1][horizonal -1] = '💲'

print(f'{row1}\n{row2}\n{row3}')