class A:

    a = 5

    def sample(self):
        print("Inside Sample Method of class A")


class B(A):

    a = 10

    def sample(self):
        print("Inside Sample Method of class B")

    def printProperties(self):
        print(super().a)                        #Inherited variable of class A
        super().sample()                        #Inherited method of class A
        print(self.a)   
        self.sample()

obj = B()
obj.printProperties()