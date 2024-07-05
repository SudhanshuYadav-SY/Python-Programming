class A:
    a = 8
    def sample_A(self):
        print("Inside Sample Method of Class A")

class B(A):
    a = 10                                              #Over-ridden variable
    def sample_A(self):                                 #Over-ridden Method
        print("Inside Sample Method of Class B")

obj = B()
print(obj.a)
obj.sample_A()