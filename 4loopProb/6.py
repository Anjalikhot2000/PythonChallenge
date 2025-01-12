# Compute the factorial of a number using while loop

num=int(input("enter a number"))
n=num
fact=1
while(num>0):
    fact=fact*num
    num=num-1

print(f"Factorial of {n} is {fact}")