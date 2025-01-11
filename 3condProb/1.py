#1. Classify a person's age group; child(<13), teenager(13 to 19), adult(20-59), Senior(60+)

def age_group(age):
    if age < 13:
        print("Child")
    elif(age <=19):
        print("Teenager")
    elif(age<60):
        print("Adult")
    else:
        print("Senior")

age=int(input("Enter your age"))
while(age<0):
    age=int(input("Enter your age"))
age_group(age)
