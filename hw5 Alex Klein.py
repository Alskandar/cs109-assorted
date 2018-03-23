##################################################
# AVERAGE NUMBERS, IGNORE STRINGS
#
# Assume we have a variable called stuff. In this variable,
# there is a list. The list contains numbers AND strings.
#
# Print the average of all of the numbers. Ignore the strings.
#

stuff = [2, "three", 4.5, -7, "dog", 3.14]

my_stuff = []

for x in stuff:
    if type(x) == int:
        my_stuff.append(x)
    if type(x) == float:
        my_stuff.append(x)
average = sum(my_stuff) / len(my_stuff)
print(average)
