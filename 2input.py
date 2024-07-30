name=input("Enter your name") #The input will be accepted in string
id= int(input("Enter your id")) #The input will be accepted in integer form
fee= eval(input("Enter your fees")) #eval() is used to parse an expression as an argument and then execute it within the Python program.
print(f"Id: {id}")
print(f"Name: {name}")
print(f"Fee: Rs.{fee}")