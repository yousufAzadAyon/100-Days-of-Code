# describe the problem
def my_function():
    for i in range(1,20):
        if i == 20:
            print("you got it")

my_function()

# reproducing error.
from random import randint
dice_imgs = ["১","২","৩","৪","৫","৬"]
dice_numbers = randint(1,6)
print(dice_imgs[dice_numbers])


# using print()
pages = 0
word_per_page = 0
pages = int(input("enter the number of page: "))
word_per_page == int(input("enter the number of world per page: "))
total_words = pages * word_per_page
print(f" pages: {pages}")
print(f"words per page: {word_per_page}")
print(total_words)


# using debugger
from typing import List


def mutate(a_list: List):
    b_list = []
    for item in a_list:
        new_item = item*2
    b_list.append(new_item) #breakpoint
    print(b_list)

mutate([1,2,3,4,5])