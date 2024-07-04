#Case 1 Lets discuss Instance Variables
class Car:
    def __init__(self,brand,model,price,milage):            #Here I have Created Instance Variables
        self.brand = brand
        self.model = model
        self.price = price
        self.milage = milage

    def startCar(self):         #An example of Instance Method
        print(self.brand+" Car having model as "+self.model+" has started")

obj1 = Car("Maruti","Swift",550000,24.0)
obj1.startCar()
obj2 = Car("Honda","Amaze",645000,16.3)
obj2.startCar()