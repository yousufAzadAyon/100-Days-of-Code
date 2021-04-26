import random
seed = int(input('create a random seed: '))
random.seed(seed)

names = input('Enter the names of the people?\n:').split()

random_number = random.randint(0, len(names)-1)

print(f'{names[random_number]} will pay the bill!')