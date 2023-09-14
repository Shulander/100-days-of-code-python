# Step 1
import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = list(random.choice(word_list))
word_length = len(chosen_word)
# Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
for i in range(word_length):
    display.append("_")
print(display)


# TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all
#  the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
def has_won(word):
    if "_" in word:
        return False
    return True


while not has_won(display):
    guess = input("Pick a letter: ").lower()

    for i in range(word_length):
        letter = chosen_word[i]
        if guess == letter:
            display[i] = letter

    print(display)

print("You win!")
