class Car :
    def sample(self,brand,model,price,milage):
        self.brand = brand
        self.model = model
        self.price = price
        self.milage = milage
        print(brand,model,price,milage)
#You can't access variables of other method in other method despite being in same class
    """def sample_two(self):
        print(brand, model, price, milage)"""
#But you can do this after implementing the following
    def sample_two(self):
        print(self.brand, self.model, self.price, self.milage)

obj1 = Car()
obj1.sample("Hyundai","i20",900000,16.5)
obj1.sample_two()