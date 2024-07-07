from abc import ABC, abstractmethod


#Class A is an Abstract class because it contains one or more abstract functions
class A(ABC):

    def __init__(self,a):           #Created Constructor for the class
        self.a = a

    #ABC is a predefined class in Python Library
    @abstractmethod
    def method_1(self):                     #Abstract Method as no function body exists
        pass
    @abstractmethod
    def method_2(self):                     #Abstract Method as no function body exists
        pass

    def method_3(self,):
        print("Inside Method 3 and value of a =",self.a)

class B(A):                             #This class will automatically become an abstract class because it's not implementing all abstract methods of parent class
    def method_1(self):
        print("Inside Method 1")

class C(B):
    def method_2(self):
        print("Inside Method 2")

#We can not create objects for Abstract Classes
#To Access Abstract methods you can create a child class and implement the same
#obj = A()
obj = C(9)
obj.method_1()
obj.method_2()
obj.method_3()