#Basic

chai="Masala Chai"
f_char=chai[0] 
print(chai) #Output:Masala Chai
print(f_char) #Output:M
slice_chai=chai[:6] 
print(slice_chai) #Output:Masala
print(chai.lower()) #Output:masala chai
print(chai.upper()) #Output: MASALA CHAI
print(chai) #Output:Masala Chai

chai=" Lemon Chai    "
print(chai.strip()) #Output:Lemon Chai

chai="Ginger Chai"
print(chai) #Output:Ginger Chai
print(chai.replace("Ginger","Black")) #Output: Black Chai

chai="Lemon,Ginger,Masala,Mint"
chai=chai.split(",")
print(chai) #Output:['Lemon', 'Ginger', 'Masala', 'Mint']

chai="Masala chai"
print(chai.find("chai")) #Output:7
print(chai.find("Chai")) #Output:-1  It means Chai is not found

chai=['Lemon', 'Ginger', 'Masala', 'Mint']
chai=" ".join(chai)
print(chai) #Output:Lemon Ginger Masala Mint

chai="Masala chai"
for i in chai:
    print(i,end=" ") #Output: M a s a l a   c h a i

#\: can be used to treat as raw
#r: can be used to treat as raw