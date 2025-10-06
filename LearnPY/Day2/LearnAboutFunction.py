#function are blocks of reuseable code that peprform specific tasks
#function គឺជាប្លុកនៃកូដ ដែលអាចប្រើឡើងវិញបាន ដែលបំពេញភារកិច្ចជាក់លាក់
'''
def function_name(parameters):
    statement
'''
def greet():
    print("Hello, my name is Sabrey")
    print("I am 20 years old")
    print("I live in Phnom Penh")
greet()

#parameter
def Hello(name):
    print(f"Your name is", name)
Hello("Sabrey")

#return value
print("Return value")
def add(a,b):
    return a+b

result =add(5,3)
print(result)

#defult parameter
print("Defult parameter")
def name(name="sabrey"):
    print(f"Your name is, {name}")
name("KoKO")