import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
end_of_game = False
word_list = ['perplex', 'banana', 'cat', 'book', 'brick']
secret_word = random.choice(word_list)
empty_list = []
life = 6

for i in range(0, len(secret_word)):
    empty_list.append('_')

while not end_of_game:
    letter = input('Guess a Letter: ')

    for index, item in enumerate(secret_word):
        if item == letter:
            empty_list[index] = letter

    if letter not in secret_word:
        life -= 1
        print(stages[life])
        if life == 0:
            end_of_game = True
            print('You lose!')

    print(empty_list)
    if '_' not in empty_list:
        end_of_game = True
        print('You Won!')


    