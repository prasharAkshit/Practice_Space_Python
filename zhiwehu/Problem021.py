"""
Question:
A robot moves in a plane starting from the original point (0,0).
The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
The trace of robot movement is shown as the following: UP 5 DOWN 3 LEFT 3 RIGHT 2 ¡
The numbers after the direction are steps. Please write a program
to compute the distance from current position after a sequence of movement and original point.
If the distance is a float, then just print the nearest integer.
Example: If the following tuples are given as input to the program: UP 5 DOWN 3 LEFT 3 RIGHT 2
Then, the output of the program should be: 2
"""
user_input_dict = dict({})
vert, horiz = 0, 0


user_input = input("Enter the distances: ").split()

for i in range(0, len(user_input), 2):
    user_input_dict[user_input[i]] = user_input[i+1]

for i in user_input_dict.keys():
    if i == "UP":
        vert += int(user_input_dict[i])
    elif i == "DOWN":
        vert -= int(user_input_dict[i])
    elif i == "LEFT":
        horiz -= int(user_input_dict[i])
    elif i == "RIGHT":
        horiz += int(user_input_dict[i])

distance = int((abs(vert)**2 +abs(horiz)**2)**0.5)
print(distance)