#Choose a mode of traansport based on the distance(eg<3km:walk,3-15:bike,>15km:car)

dis=int(input("Enter distance:"))

if dis<=0:
    print("Invalid distance")
    exit()
if dis<3:
    print("Walk")
elif dis<15:
    print("Bike")
else:
    print("Car")