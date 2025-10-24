"Encapsulation គឺជា concept ដែល concept ទាក់ទងនឹងការយក function និង attibute ទៅដាក់ក្នុង class តែមួយជាមួយគ្នា។​ ហើយអាច set field ណាមួយទៅជា private field។" 

class Person:
    def __init__(self,name,age):
        self.name = name #public
        self.__age = age #private
    
    def get_age(self):
        return self.__age
    
person1 = Person("sabrey",20)
print(person1.name)
print(person1.get_age())