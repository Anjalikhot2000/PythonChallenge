#Assign a letter grade based on student's score: A(90-100), B(80-89), C(70-79), D(60-69), F(below 60)

marks=int(input("Enter marks:"))

if marks>=101:
    print("Invalid marks")
else:
    if(marks<60):
        grade= "F"

    elif(marks<70):
        grade= "D"

    elif(marks<80):
        grade= "C"

    elif(marks<90):
        grade= "B"

    else:
        grade= "A"
    
    print(f"grade= {grade}")