#Write a function that greets a user. If no name is provided, it should greet with default name.

def greet(name="Anjali"):
    return f"Hello,{name}"

print(greet())
print(greet("Aditya"))