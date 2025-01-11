#Customize a coffee order:small,medium or large with an extra short of espresso

size=input("Enter coffee size(small,medium or large):").strip().lower()
extra_short=input("Want extra short(y/n)").strip().lower()
s=["small","medium","large"]

if size not in s:
    print("Invalid size")
    exit()
    
if extra_short=="y" or extra_short=="yes":
    print(f"Your coffee order is: {size} with extra short of espresso")
elif extra_short=="n" or extra_short=="no":
    print(f"Your coffee order is: {size} with no extra short of espresso")
else:
    print("Invalid input")