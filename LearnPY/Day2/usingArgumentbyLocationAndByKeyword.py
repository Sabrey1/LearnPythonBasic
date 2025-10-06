#Using Argument by Location And By Keyword

#positional argument
def greet(name,message):
    print(f"Hello, {name}! {message}")
greet("Sabrey","Good morning")

#keyword argument
def greet1(names,messages):
    print(f"Hello, {names} ! {messages}")
greet1(messages="Good morning",names="Sabrey")