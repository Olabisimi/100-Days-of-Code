# Define a function to turn_right, it only turn_left
def turn_right():
    turn_left()
    turn_left()
    turn_left()
# Keep running the loop until it reaches the goal
while not at_goal():
# If no wall on the right, turn right and move forward
    if right_is_clear():
        turn_right()
        move()
# If right is not clear but the front is open, move
    elif front_is_clear():
        move()
# If both right and front are blocked, turn left
    else:
        turn_left()
