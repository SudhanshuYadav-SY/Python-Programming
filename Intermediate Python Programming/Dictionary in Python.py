car ={
    "Brand":"Honda",
    "Model":"Amaze",
    "Price": 900000,
    "Milage":14.65
}
print("Output as per Case 1")
print(car)
print(type(car))
#Case 2 Find value of one the key
print("Output as per Case 2")
print(car.get("Price"))             #Get the Price of Car
print(car["Model"])                 #Get the Model of Car
#Case 3 Print all keys or values of dictionary
print("Output as per Case 3")
print(car.keys())
print(car.values())
#Case 4 Updating the values of dictionary
print("Output as per Case 4")
print(car)
car["Price"] = '660000'     #Hence Proved dictionary is mutable
print(car)
#Case 5 Add a New Key to dictionary
print("Output as per Case 5")
print(car)
car["color"] = "Black"
print(car)
#Case 6 Use for each loop in Dictionary
print("Output as per Case 6")
for k in car:
    print(k)
#Alternatively you can use this,
"""for j in car.keys():
    print(j)"""
for j in car.values():
    print(j)
#Alternatively you can try this out,
print("Special Case")
for a in car.keys():
    print(a,car.get(a))                 #Here Key-value pair will be printed

#Case 7 Items in Dictionary
print("Output as per Case 7")
for d,e in car.items():
    print(d,e)                          #Here Key-value pair will be printed

#Case 8 Pop item from dictionary
print("Output as per Case 8")
print(car)
#car.pop("color")
#print(car)

#Alternatively you can use del keyword

#Case 9 Removing the last item
print("Output as per Case 9")
print(car)
#car.popitem()
#print(car)

#Case 10 Clear all items from dictionary
print("Output as per Case 10")
print(car)
car.clear()
print(car)