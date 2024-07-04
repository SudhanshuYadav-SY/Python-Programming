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
obj1.parent_method()
obj1.child_method()

#Case 2 Implementation of Multilevel Inheritance
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tImplementation of Multilevel Inheritance . . .")
class GrandChild(Child):
    def GrandChildMethod(self):
        print("Inside Grand Child Method of Grand Child Class")


obj2 = GrandChild()
obj2.parent_method()
obj2.child_method()
obj2.GrandChildMethod()

#Case 3 Implementation of Hierarchical Inheritance
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tImplementation of Hierarchical Inheritance . . .")
class GrandChild2(Parent):
    def GrandChildMethod2(self):
        print("Inside 2nd Grand Child Method of Grand Child Class")

obj3 = GrandChild2()
obj3.GrandChildMethod2()
obj3.parent_method()