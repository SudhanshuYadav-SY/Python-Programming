class A:
    a = 5                                           #Normal Variable
    def sample(self):                               #Normal Method
        print(self.a)
        print("-----------------------------------------------------")
    __b = 17                                        #Private Variable
    def __samplePvt(self):                          #Private Method
        print("Inside Private Method of Class A")


    def print_Details(self):
        print(self.__b)                             #Calling out Private Variable "b" of class A
        self.__samplePvt()                          #Calling out Private Method of class A


obj = A()
obj.sample()
obj.print_Details()
