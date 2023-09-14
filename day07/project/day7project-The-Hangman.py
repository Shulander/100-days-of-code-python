# Step 1
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

word_list = ["aardvark", "baboon", "camel"]
chosen_word = list(random.choice(word_list))
word_length = len(chosen_word)
# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#  Set 'lives' to equal 6.
# start live count
lives = 6

# create display
display = []
for i in range(word_length):
    display.append("_")
print(display)


def has_won(word):
    return "_" not in word


def has_lives():
    return lives > 0


while not has_won(display) and has_lives():
    guess = input("Pick a letter: ").lower()

    for i in range(word_length):
        letter = chosen_word[i]
        if guess == letter:
            display[i] = letter

    # TODO-2: - If guess is not a letter in the chosen_word,
    #  Then reduce 'lives' by 1.
    #  If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        print(f"letter '{guess}' is not in the word. You have lost a live!")
        lives -= 1

    print(' '.join(display))
    print(stages[lives])

if has_lives():
    print("You win!")
else:
    print("You lose!")
