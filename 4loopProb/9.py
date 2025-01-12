#Check if all elements in a list are unique.If a duplicate is found, exit the loop and print duplicate

items=["apple","banana","orange","apple","mango"]
dup=False
for i in items:
    if items.count(i)>1:
        dup=True
        break
if dup==True:
    print("Duplicate found")
else:
    print("No duplicates")

        