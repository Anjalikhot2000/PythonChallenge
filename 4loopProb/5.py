#Given a string, find the first non-repeated character

name=input("Enter a string").strip()

for i in name:
    if name.count(i)==1:
        print(i)
        break
