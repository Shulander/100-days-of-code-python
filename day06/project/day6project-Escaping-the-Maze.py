# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# Write a program using an if/elif/else statement so Reeborg can find the exit. The secret is to have Reeborg follow along the right edge of the maze, turning right if it can, going straight ahead if it can’t turn right, or turning left as a last resort.
# What you need to know
#     The functions move() and turn_left().
#     Either the test front_is_clear() or wall_in_front(), right_is_clear() or wall_on_right(), and at_goal().
#     How to use a while loop and if/elif/else statements.
#     It might be useful to know how to use the negation of a test (not in Python).

def turn_right():
    turn_left()
    turn_left()
    turn_left()


# Fix the look when robot get stuck turing right
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
    elif not front_is_clear():
        turn_left()
    if front_is_clear():
        move()
