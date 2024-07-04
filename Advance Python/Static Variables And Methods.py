#Case 1 Lets discuss Static Variables
class Car:
    wheels = 4                                              #Here I have created a particular static variable

    @staticmethod
    def printCarWheels():
        print(Car.wheels)                               #To Access a static variable you have to use class name

obj1 = Car()
print(Car.wheels)