tea_varities =["black","green","oolong","white"]
print(tea_varities) #Output: ['black', 'green', 'oolong', 'white']
print(tea_varities[0])  #Output: black
print(tea_varities[-1]) #Output: white
print(tea_varities[1:3]) #Output: ['green', 'oolong']
print(tea_varities[:2]) #Output: ['black', 'green']
print(tea_varities[::2]) #Output: ['black', 'oolong']
tea_varities[3]="herbal"
print(tea_varities) #Output: ['black', 'green', 'oolong', 'herbal']
tea_varities[1:2] = ["Lemon"]
print(tea_varities) #Output: ['black', 'Lemon', 'oolong', 'herbal']
tea_varities[1:3] = ["green","masala"]
print(tea_varities) #Output: ['black', 'green', 'masala', 'herbal']
for tea in tea_varities:
    print(tea) #Output: black green masala herbal
if "oolong" in tea_varities:
    print("oolong is in the list") #Output: nothing will be printed
tea_varities.append("oolong") # add "oolong" at the last
if "oolong" in tea_varities:
    print("oolong is in the list") #Output: oolong is in the list