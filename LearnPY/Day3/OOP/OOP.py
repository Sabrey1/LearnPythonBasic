# Object-Oriented Programming (OOP) is a power ful way to structure your code by creating objects that represent real-world things.

# class
class Car:
    #constructor method
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.color = "red"
    
    def display_info(self):
        return f"{self.make} {self.model} {self.year}"

#object
car1 = Car("Toyota","Corolla",2020)
car2  = Car("Honda","Civic",1999)
print(car1.display_info())
print(car2.display_info())

#attributes
print(car1.color)

