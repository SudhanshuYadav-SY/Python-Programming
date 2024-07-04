#Case 1 Single Inheritance
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tImplementation of Single Inheritance . . .")
class Parent:
    a = 9
    def parent_method(self):
        print("Inside Parent Method of Parent Class")


class Child(Parent):                            #Here, Child is inheriting properties of Parent Class
    b = 10
    def child_method(self):
        print("Inside Child Method in Child Class")


obj1 = Child()
print(obj1.a)
obj1.parent_method()
print(obj1.b)
obj1.child_method()

#Case 2 Implementation of Multilevel Inheritance
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tImplementation of Multilevel Inheritance")