class Car:
    wheels = 4
    def start_car(self):
        print("Car Started!!")
    def example(self):
        #print(wheels)              #This will give error as you can't use it like that as per Syntax
        print(self.wheels)          #This will NOT give error as you use it like that as per Syntax
        self.start_car()
#Using Object Reference we can access the properties of object outside the class
obj1 = Car()
print(obj1.wheels)
obj1.start_car()
obj1.example()
#Hence it can be said that,
# if you want to use a variable or method inside the same class,
# then you need to refer that variable or method by using "self" keyword
# as shown in above examples for your consideration.