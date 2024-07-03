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
#Case 3 Print all keys of dictionary