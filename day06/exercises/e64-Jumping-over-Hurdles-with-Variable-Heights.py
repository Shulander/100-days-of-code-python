# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
#
# You should be able to write programs that are valid for worlds Around 4 and Hurdles 3,
# and ot combine them for this last hurdles race.
# Your program should also be valid for worlds Hurdles 1, Hurdles 2 et Hurdles 3

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if front_is_clear():
        move()
    else:
        jump()
