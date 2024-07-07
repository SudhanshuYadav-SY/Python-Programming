import math
import random

print("Square Root of 25= "+str(math.sqrt(25)))
print("Value of Pi = "+str(math.pi))
print("2 to the power 10 = "+str(math.pow(2,10)))


#Case 2 Random Selection
colors = [
    "Red",
    "Blue",
    "Green",
    "Yellow",
    "Orange",
    "Purple",
    "Pink",
    "Brown",
    "Black",
    "White",
    "Gray",
    "Cyan",
    "Magenta",
    "Maroon",
    "Olive",
    "Navy",
    "Teal",
    "Lavender",
    "Turquoise",
    "Beige",
    "Coral",
    "Indigo",
    "Gold",
    "Silver",
    "Peach"
]

print("Random Colour Selected = "+random.choice(colors))