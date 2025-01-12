#Print the multiplication table for a given number upto 10,but skip the 5th iteration
num=int(input("Enter a number"))
for i in range(1,11):
    if i!=5:
        print(f"{num}x{i}={num*i}")

