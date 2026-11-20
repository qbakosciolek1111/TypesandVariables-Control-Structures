###
# Generates and prints a random number between 1 and 6,
# similar to rolling a dice
#
import random

dice = random.randint(1, 6)  # randint(a, b) losuje liczbę całkowitą z OBU końcami włącznie, więc 6 też może wypaść; random.randrange(1, 6) nigdy nie dałoby 6
print('You rolled', dice)