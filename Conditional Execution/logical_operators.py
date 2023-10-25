# In Python, logical operators are used to evaluate expressions and return a Boolean
# value (True or False). The logical operators in Python are and, or, and not.

a = 5
is_betweeen = a < 10 and a > 0
print(is_betweeen) #True


# Imagine we are building a system to control a smart home, and we want to turn on
# the lights in a room either if it's dark or if someone is in the room.
# Variables to store sensor data
is_dark = False  # Light sensor says it's not dark
someone_in_room = True  # Motion sensor detects someone in the room

# Turn on lights if it's dark or if someone is in the room
if is_dark or someone_in_room:
    print("Turning on the lights.")
else:
    print("No need to turn on the lights.")
