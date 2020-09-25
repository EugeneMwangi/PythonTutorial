# Variables
# Import header files
from math import *
character_name = "Eugene"
character_age = 25

# The + sign can be used to append a string to another string
# This is called concatenating
# ##### Strings and their functions #####
phrase = "Welcome to my channel"
print("Hello World, my name is \"" + character_name + "\".")
print("I am " + str(character_age) + " years old.")
# Convert string entirely to lower case
print(phrase.lower())
# Convert string to entirely upper case
print(phrase.upper())
# Check if string is upper case
print("Is string in upper case? \"" + str(phrase.isupper()) + "\"")
# Using the functions one after the other
# We shall convert the string to upper case
# then check to see if it is in upper case
print("Is string in upper case after conversion? \""+str(phrase.upper().isupper()) + "\"")
# Find the length of a string
print("Length of string: " + str(len(phrase)))
# Obtaining the individual characters
print("The first character of the string is \'" + phrase[0] + "\'")
# Obtain the index of a character in a string
print("Index of \"o\" is " + str(phrase.index("o")))
# Replace a character or part of the string
print("Replace \"my\" with \"his\": " + phrase.replace("my", "his"))
print(phrase)

# ##### Numbers and their Functions #####
my_num = -5
# Get the absolute value of a number
print("The absolute number is " + str(abs(my_num)))
# Obtain power of a number
print("4 to the power of 6 is " + str(pow(4, 6)))
# Return the largest number in an array
print("The larger number is " + str(max(2, 4, 5, 6, 5, 8)))
# Round a number
print("Round of 3.2 is " + str(round(3.2)))
print("Round of 3.6 is " + str(round(3.6)))

# *** Using functions from the math header *** #
# Round down a number
print("Round down 3.7: " + str(floor(3.7)))
# Round up a number
print("Round up 3.2: " + str(ceil(3.2)))
# Find square root
print("Sqrt of 36: " + str(sqrt(36)))

# #### Obtaining Input from User #### #
# Prompt user to enter name and store it in variable name
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello "+name+"! You are "+age)



