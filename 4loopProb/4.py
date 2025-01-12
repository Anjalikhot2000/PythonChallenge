#Reverse a string using loop

s=input("Enter a string").strip()
rev=""
for i in s:
    rev=i+rev
print(rev)
