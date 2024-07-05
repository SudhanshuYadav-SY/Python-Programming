"""Encapsulation is a process of binding both private variables with methods in a single way
in such a way that you can access or modify the private methods or variables using the
concept of Getters & Setters outside the class . . .


To implement the same check the program below for practical demonstration"""

class A:
    __age = 0                                     #Private Variable


    def set_Age(self,age):                      #This method will set the Age
        A.__age = age


    def get_Age(self):                          #This Method will get the Age
        return A.__age


obj = A()
obj.set_Age(26)                                                 #This "25" will be passed to the corresponding age in setter function mentioned above by the name "set_Age()"
print("Age of the User = "+str(obj.get_Age()))                  #This will successfully print the age as passed in the previous statement and will get the result on your console using "get_Age()"