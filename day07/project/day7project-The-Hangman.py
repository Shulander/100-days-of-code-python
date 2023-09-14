import random
from replit import clear

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#  Delete this line: word_list = ["ardvark", "baboon", "camel"]
from hangman_words import word_list
from hangman_art import logo, stages

chosen_word = list(random.choice(word_list))
word_length = len(chosen_word)
# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# start live count
lives = 6
# already used letters
guessed_letters = []

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)

# create display
display = []
for i in range(word_length):
    display.append("_")
print(display)


def has_won(word):
    return "_" not in word


def has_lives():
    return lives > 0


def read_player_guess():
    new_guess = input("Pick a letter: ").lower()
    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    while new_guess in guessed_letters:
        print(f"You have already picked the letter '{new_guess}', please chose a new letter")
        print("Already picked letters: " + ', '.join(guessed_letters))
        new_guess = input("Pick a letter: ").lower()
    guessed_letters.append(new_guess)
    return new_guess


while not has_won(display) and has_lives():
    # read customer's guess
    guess = read_player_guess()

    clear()

    # Check guessed letter
    for i in range(word_length):
        letter = chosen_word[i]
        if guess == letter:
            display[i] = letter

    if guess not in chosen_word:
        # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed '{guess}', that is not in the word. You lose a live!")
        lives -= 1

    print(' '.join(display))
    # TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])

if has_lives():
    print("You win!")
else:
    print("You lose!")
