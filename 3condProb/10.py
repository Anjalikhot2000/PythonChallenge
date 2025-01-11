#Recommend a pet food based on the pet's age and species (eg: Dog:<2 years:Puppy food, cat>5yrs -Senior cat food)

pet=["dog","cat"]

species=input("Enter the species of the pet:").strip().lower()
age=int(input("Enter the age of the pet:"))

if species in pet:
    if species=="dog":
        if age<2:
            print("Puppy food is recommended for your pet")
        else:
            print("Adult dog food is recommended for your pet")
    else:
        if age>5:
            print("Senior cat food is recommended for your pet")
        else:
            print("Kitten food is recommended for your pet")
else:
    print("Invalid species entered. Please enter either dog or cat")
