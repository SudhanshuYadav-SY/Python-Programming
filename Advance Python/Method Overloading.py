class A:
    def sample(self):
        print("Inside Sample Method 1")

    def sample(self,a):                     #Method Over-loaded
        print("Inside Sample Method 2 and the value of a = ",a)

obj = A()
obj.sample(7)