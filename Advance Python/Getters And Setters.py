class A:
    __age = 0                                     #Private Variable


    def set_Age(self,age):                      #This method will set the Age
        A.__age = age


    def get_Age(self):                          #This Method will get the Age
        return A.__age


obj = A()
obj.set_Age(25)                 #this "25" will be passed to the corresponding age in setter function mentioned above by the name "set_Age()"
print(obj.get_Age())            #This will successfully print the age as passed in the previous statement and will get the result on your console using "get_Age()"