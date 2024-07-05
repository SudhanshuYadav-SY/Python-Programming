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
print("----------------------------------------------------------------------------------------------------------")
#Case 2

class H:
    def __init__(self):
        print("Init Method for class A")


class J(H):
    pass                #Nothing will happen just class will be passed


J()
print("----------------------------------------------------------------------------------------------------------")
#Case 3
class M:
    def __init__(self):
        print("Init method of class M")

class O(M):
    def __init__(self):
        print("Init Method of class O")
        super().__init__()

O()