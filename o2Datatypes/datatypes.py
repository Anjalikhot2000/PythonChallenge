a= 2 #number
import math
print(math.pi) #Output: 3.141592653589793
import random
print(random.random()) #prints random number
print(random.choice([1,22,3,4,56,7])) #print random number from the given list


# String
username="Anjali"
print(len(username)) #Output:6
print(username[0]) #Output:A
#String is mutable and doesnot support item assingment
print(username[1:3]) #slicing, Output:nj
print(dir(username)) #contains all functions

#List
myList=[123,"Anjali",3.142]
print(myList) #Output:[123,"Anjali",3.142]
print(len(myList)) #Output:3

#dictionary
myD={"One":"Lemon","two":"ginger","three":"black"} 
print(myD) #Output:{"One":"Lemon","two":"ginger","three":"black"}
print(myD["One"]) #Output:Lemon


#Tuples
myTuple=(1,2,3,4,5)
print(myTuple) #Output:(1,2,3,4,5)
print(myTuple[0]) #Output:1
print(len(myTuple)) #Output:5


