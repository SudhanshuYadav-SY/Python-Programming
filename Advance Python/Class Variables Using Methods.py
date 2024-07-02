class Car:
    def _intialize_method(self,brand,model,price,milage):
        self.brand = brand
        self.model = model
        self.price = price
        self.milage = milage

    def start_Car(self):
        print("I own a "+self.brand+" car its brand is "+self.model+" and currently its running on roads")

    def stop_car(self):
        print("I own a " + self.brand + " car its brand is " + self.model + " and currently it is stopped")

    def print_car_details(self):
        print("I own a " + self.brand + " car its brand is " + self.model + " its price is "+str(self.price)+" and this car has a milage of "+str(self.milage))


obj1 = Car()
print("Output from Object 1 . . .")
obj1._intialize_method("Tata","Neu",850000,20.0)
obj1.start_Car()
obj1.stop_car()
obj1.print_car_details()
print("---------------------------------------------------------------------------------------------")
obj2 = Car()
print("Output from Object 2 . . .")
obj2._intialize_method("Maruti","Suzuki 800",350000,15.0)
obj2.start_Car()
obj2.stop_car()
obj2.print_car_details()
print("----------------------------------------------------------------------------------------------")
obj3 = Car()
print("Output from Object 3 . . .")
obj3._intialize_method("Maruti","Suzuki 800",350000,15.0)
obj3.start_Car()
obj3.stop_car()
obj3.print_car_details()
print("----------------------------------------------------------------------------------------------")