#Inheritance
# super class (parent class)
# sub class (child class)

class animal:
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        return f"{self.name} make a sound."

class dog(animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
    
    #method overiding
    def speak(self):
        return f"{self.name} barks."

class Cat(animal):
    def __init__(self,name,color):
        super().__init__(name)
        self.color = color
    
    #method overiding
    def speak(self):
        return f"{self.name} meows."


#object 
mydog = dog("Buddy","Golden Retriever")
print(mydog.name)
print(mydog.breed)
print(mydog.speak())

#object 
mycat = Cat("Whiskers","Black")
print(mycat.name)
print(mycat.color)
print(mycat.speak())