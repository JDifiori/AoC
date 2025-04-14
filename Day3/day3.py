
# Day 3 solution script 
# Step approach to solve the problem
# read file and locate all "mul" strings
# save all instances of "mul ()" to a list 
# check instance to see if it is valid 
# if not valid, drop
# perform multiplication if valid and add to sum

# import the regex module to use regex for string manipulation
import re 

file = open(r'C:\Users\joshu\Documents\AoC\Day3\d3input.txt')

# Get the file contents as a string
text = file.read()

# Using this approach to drop everything that isn't a "mul" string
translation_table = dict.fromkeys(map(ord, "abcdefghijknopqrstvwxyz!<>}&/{,@#$*-\':;+=-%~?[]^'"), None)

# Remove all characters that are not digits or "mul"
text = text.translate(translation_table)







file.close()