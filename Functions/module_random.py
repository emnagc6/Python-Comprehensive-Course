#The random module in Python is used to generate pseudo-random numbers for various 
#distributions including integer, float (real numbers), and sequences. It is an extremely 
#useful module for simulation, testing, and gaming, among other things.

# Python's random module uses the Mersenne Twister as its core generator. It produces 
# 53-bit precision floats and has a period of 219937−1219937−1, which is a Mersenne prime.

import random

random_number = random.randint(0,100)
print(random_number)

random_float = random.random()
print(random_float) #generates a float number between 0 and 1.

#let's generate a number random between 0 and 5
my_random = random.random() * 5
print(my_random)