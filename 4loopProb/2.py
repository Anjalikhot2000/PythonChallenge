#Calculate the sum of even numbers up to a given number n.

num=int(input("Enter a number:"))
sum=0

for i in range(num+1):
    if i%2==0:
        sum+=i
print("Sum of even numbers=",sum)
