#Check if a password is weak,medium or strong. criteria<6:weak,6-10:medium,>10:strong

password=input("enter password:").strip()
length=len(password)

if length<6:
    print("Weak")
elif length<10:
    print("Medium")
else:
    print("Strong")