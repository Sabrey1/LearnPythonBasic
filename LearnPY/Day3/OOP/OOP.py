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


#class
# class Persion:
#     def __init__(self,name,age,city):
#         self.name = name
#         self.age = age
#         self.city = city
#     def display_info(self):
#         return f" My name is {self.name}. I am {self.age} years old. I live in {self.city}."

# object
# persion1 = Persion("sabrey",20,"Siew Reap")
# print(persion1.display_info())

