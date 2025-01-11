#Dictionary is unordered
chai_types = {"Masala":"spicy", "Ginger":"zesty", "Green":"mild"} #or dict()

#Accessing
print(chai_types["Masala"]) #prints: spicy we can even access chai_types.get("Ginger")
print(chai_types.get("Ginger"))
chai_types["Green"]="fresh"
print(chai_types)

for chai in chai_types:
    print(chai, chai_types[chai]) #prints: Masala Ginger Green

for key,value in chai_types.items():
    print(key,value) #prints: Masala spicy Ginger zesty Green mild

if "Masala" in chai_types:
    print("yes")

print(len(chai_types)) #prints: 3

chai_types["Earl Grey"] ="citrus"
print(chai_types)

chai_types.pop("Ginger")  #for last item to be popped we use chai_types.popitem(), del(chai_type["Green"]) method is also used
print(chai_types)

tea_shop={
    "chai":{"Masala": "spicy", "Ginger":"zesty"},
    "tea":{"Green":"mild","black":"strong"}
    }
print(tea_shop)
print(tea_shop["chai"])
print(tea_shop["chai"]["Masala"])

sq_num={x:x**2 for x in range(5)}
print(sq_num)

names=["Ironman","thor","spiderman"]
default=90
new_dict=dict.fromkeys(names,default)
print(new_dict)