#Suggest activities based on weather conditions (eg-Sunny:go for walk, rainy:read a book, snowy: build a snowman)

activities={"sunny":"Go for a walk","rainy":"read a book","snowy":"Build a snowman"}

weather=input("enter wheather").strip().lower()
if weather in activities:
    print(activities[weather])
else:
    print("Invalid input")