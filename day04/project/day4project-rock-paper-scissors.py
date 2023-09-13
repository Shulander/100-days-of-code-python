import random

rock = '''
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = ''' 
Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
drawings = [rock, paper, scissors]

result = [["Draw", "Loose", "Win"], ["Win", "Draw", "Loose"], ["Loose", "Win", "Draw"]]
result2 = ["Draw", "Loose", "Win"]

user_pick = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")) % 3
computer_pick = random.randint(0, 2)

print("Your choice:")
print(drawings[user_pick])
print("Computer choice:")
print(drawings[computer_pick])

print(f"Matrix solution: You {result[user_pick][computer_pick]}!")
print(f"List solution: You {result2[(computer_pick - user_pick) % 3]}!")
