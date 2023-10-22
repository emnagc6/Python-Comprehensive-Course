# In Python, we can use multiple independent if statements to test different 
# conditions in a non-mutually exclusive manner. Unlike chained conditionals 
# (if, elif, else) that evaluate conditions in a sequence and break after the 
# first true condition, multiple if statements allow for the possibility that
# more than one condition can be true, and therefore, multiple code blocks can execute.

speed = 90
agility = 85
strength = 75

# Chained conditional for overall performance
if speed + agility + strength > 240:
    print("Robot is excellent")
elif speed + agility + strength > 180:
    print("Robot is good")
else:
    print("Robot needs improvement")

# Multiple if statements for individual attributes
if speed > 80:
    print("Robot has high speed")
  
if agility > 80:
    print("Robot is highly agile")

if strength > 80:
    print("Robot is very strong")
