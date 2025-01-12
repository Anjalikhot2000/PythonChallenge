#Check if a number is prime

number=int(input("Enter a number"))
is_Prime=True
if number>1:
    for i in range(2,number):
        if number%i==0:
            is_Prime=False
            break
if is_Prime==True:
    print(number,"is a prime number")
else:
    print(number,"is not a prime number")