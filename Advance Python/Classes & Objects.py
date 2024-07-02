#This is an example of Function in Python
"""def sample_Function():
    print("Inside Sample Function")"""
class Car:
    wheels = 4
#This is an example of Method in Python
    def start_car(self):
        print("Car Has Started!!")
    def stop_car(self):
        print("Car Has Stopped!!")

obj_Car1 = Car()           #This statement is creating an object for class Car
print("Output as Per Object 1")
print(obj_Car1.wheels)
print(obj_Car1.start_car())
obj_Car2 = Car()
print("Output as Per Object 2")
print(obj_Car2.wheels)
print(obj_Car2.stop_car())