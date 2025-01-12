#Create a function that returns both area and circumference of a circle given its radius.

def circle(r):
    area=3.142*r*r
    circum=2*3.142
    return area,circum

r=int(input("Enter radius:"))
area,circum=circle(r)
print(f"Area={area}\nCicumferences={circum}")