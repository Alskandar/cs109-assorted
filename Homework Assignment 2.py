###############################
# GRADE
#
# Given the score (0 to 100) received on a test, print the letter grade.
# You can just give the letter, no need for the +/-
#
# The score should be taken from user input.
#
# In case you have been at Hampshire long enough to forget how grades work,
# you can use the first table on this wikipedia page:
# https://en.wikipedia.org/wiki/Academic_grading_in_the_United_States

### YOUR CODE HERE ###

score = input("Enter your score here.")

if int(score) > 100 or int(score) < 0:
    print("Invalid score.")
elif int(score) > 89:
    print("You got an A!")
elif int(score) > 79:
    print("You got a B.")
elif int(score) > 69:
    print("You got a C.")
elif int(score) > 59:
    print("You got a D.")
else:
    print("You got an F.")

###############################
# AREA
#
# Take user input to determine the name of a shape (rectangle or triangle)
#
# Depending on the shape name, create as many variables as needed and set their
# values based on user input.
#
# Print the area of the shape.

### YOUR CODE HERE ###

shape = input("Triangle or rectangle?")

if str(shape) == "Triangle" or str(shape) == "triangle":
    base = input("Length of base")
    height = input("Height of triangle")
    area = (int(base) * int(height)) / 2
    print("The area of your triangle is " + str(area)+ " units squared.")
elif str(shape) == "Rectangle" or str(shape) == "rectangle":
    length = input("Length of rectangle")
    height = input("Height of rectangle")
    area = int(length) * int(height)
    print("The area of your rectangle is " + str(area)+ " units squared.")
else:
    print("Invalid shape")
