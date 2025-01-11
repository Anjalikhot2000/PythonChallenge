# 2.Movie tickets are prices based on age:$12 for adults(18 or above),$8 for children. Everyone gets $2 discount on wed
    

age=int(input("enter age:"))
day=input("Is it wednesday(y/n):")

#Type1:
# price=12 if age>=18 else 8
# if day.lower()=="y":
#     price-=2

# print(f"The price ticket is $ {price}")



#Type2:
if (day.lower()=="y" or day.lower()=="yes"):
    if age >=18:
        price= 12-2
        print(f"The price of the ticket is ${price} for adult")
    else:
        price= 8-2,"child"
        print(f"The price of the ticket is ${price} for adult")
elif (day.lower()=="n" or day.lower()=="NO"):
    if age >=18:
        price= 12,"adult"
        print(f"The price of the ticket is ${price} for adult")
    else:
        price= 8,"child"
        print(f"The price of the ticket is ${price} for adult")
else:
    print("invalid input")


