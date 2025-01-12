#Given a list numbers, count how many are positive numbers.
#numbers=[1,-2,3,-4,5,6,-7,-8,9,10]

numbers=[1,-2,3,-4,5,6,-7,-8,9,10]
positive_numbers=[]

for i in numbers:
    if i>0:
        positive_numbers.append(i)

c=len(positive_numbers)
print(f"The count of positive numbers:{c}")