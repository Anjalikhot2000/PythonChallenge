#Immutable
tea_types =("masala","black","green")
print(tea_types)

print(len(tea_types)) #Output:3
more_tea =("Herbal","Earl grey")
all_tea= tea_types+more_tea
print(all_tea) #output: ('masala', 'black', 'green', 'Herbal', 'Earl grey')
more_tea=("herbal","Earl grey","herbal")
print(more_tea.count("herbal"))

marks=(90,8-0,70)
(a,b,c)=marks
print(b)