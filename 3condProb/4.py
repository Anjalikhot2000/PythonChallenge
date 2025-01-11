#Determine if a fruit is ripe,overripe or unripe based on its color.(eg:Banana: green-Unripe,yellow-ripe,brown-overripe)

color=input("enter the color of the fruit(green/yellow/brown):")

if color.lower()=="green":
    print("unripe")
elif color.lower()=="yellow":
    print("ripe")
elif color.lower()=="brown":
    print("overripe")
else:
    print("invalid input")
