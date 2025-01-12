#Keep asking the user for input until they enter a number between 1 and 10

n=int(input("Enter a number between 1 and 10"))
while n>10 or n<=0:
    n=int(input("Enter number again between 1 and 10"))

print(f"The entered number is{n}")
